import os
from multiprocessing import Pool

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string  
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Article

from .forms import URLForm

from news.scripts.nlp import predict_on_text
from news.scripts.model_loader import ModelLoader



class IndexView(generic.ListView):
    template_name = "news/index.html"
    context_object_name = "latest_article_list"

    def get_queryset(self):
        """Return the last five published articles."""
        article_list = (
            Article.objects.filter(source_site='Site 1').filter(scraped_date__lte=timezone.now()).order_by("-scraped_date")[:5]   
        )
        return article_list


class DetailView(generic.DetailView):
    model = Article
    template_name = "news/detail.html"
    def get_queryset(self):
        return Article.objects.filter(scraped_date__lte=timezone.now())
    
    
class BrowseView(generic.TemplateView):
    template_name = "news/browse.html"

    def get_context_data(self, **kwargs):
        context = super(BrowseView, self).get_context_data(**kwargs)
        context['latest_article_list'] = Article.objects.filter(scraped_date__lte=timezone.now()).order_by("-scraped_date")[:10]
        context['date_today'] = timezone.now().date().strftime("%Y-%m-%d")
        context['date_week_ago'] = (timezone.now() - timezone.timedelta(days=7)).date().strftime("%Y-%m-%d")
        return context









def check_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            model_loader = ModelLoader()

            # Access the loaded models
            scraper = model_loader.scraper
            model_w2v = model_loader.model_w2v
            predictive_model = model_loader.predictive_model
            vertex = model_loader.vertex
            llm = model_loader.llm
            
            
            scraped_data = scraper.scrape(url)
            title = scraped_data['title']
     
            try:
                article = get_object_or_404(Article, title=scraped_data['title'], source_site=scraped_data['source_site'])
            except:
                # Create a new article if no matching article exists
                with Pool(processes=3) as pool:
                    clickbait_decision_NLP = pool.apply_async(classify_NLP, (title, predictive_model, model_w2v))
                    clickbait_decision_LLM = pool.apply_async(classify_LLM, (title, llm))
                    clickbait_decision_VERTEX = pool.apply_async(classify_VERTEX, (title, vertex))

                    # Get the results
                    try:
                        results = [res.get() for res in [clickbait_decision_NLP, clickbait_decision_LLM, clickbait_decision_VERTEX]]
                    except Exception as e:
                        # Handle exception
                        print(f"An error occurred: {e}")

                # Assign the results
                clickbait_decision_NLP, clickbait_decision_LLM, clickbait_decision_VERTEX = results
                
                article = Article(
                    title=scraped_data['title'],
                    content_summary=scraped_data['content'],
                    url_from=url,
                    source_site=scraped_data['source_site'],
                    clickbait_decision_NLP = clickbait_decision_NLP,
                    clickbait_decision_LLM = int(clickbait_decision_LLM),
                    clickbait_decision_VERTEX = clickbait_decision_VERTEX,
                    clickbait_decision_final = clickbait_decision_NLP,
                )
                
            
            article.save()
            html_content = render_to_string('news/article_info.html', {'article': article})
            return JsonResponse({'html': html_content})    
    else:
        form = URLForm()

    return render(request, 'news/check_url.html', {'form': form})



def classify_NLP(data, predictive_model, model_w2v):
    proba_cutoff = 0.5
    clickbait_decision_NLP_proba = predict_on_text(predictive_model, model_w2v, data)
    clickbait_decision_NLP_proba = clickbait_decision_NLP_proba[0][1]
    return int(clickbait_decision_NLP_proba > proba_cutoff)

def classify_LLM(data, llm):

    return llm.predict(data)

def classify_VERTEX(data, vertex):
    # clickbait_decision_VERTEX = VertexAI().run(title=data)
    return 1