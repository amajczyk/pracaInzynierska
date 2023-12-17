import os
from django.conf import settings
from news.scripts.scraping import Scraper
from transformers import pipeline
from news.scripts.nlp import Word2VecModel, return_best_model, load_predictive_model
from news.scripts.llm import LocalLLM
from news.vertex.cloud.connections_based_on_docs import VertexAI

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ModelLoader(metaclass=Singleton):
    def __init__(self):
        # load Scraper
        config_path = os.path.join(settings.BASE_DIR, 'news', 'config', 'site_variables_dict')
        self.scraper = Scraper(config_path)
        
        # Load best Word2Vec model
        model_settings_path = os.path.join(settings.BASE_DIR, 'news', 'config', 'model_settings.json')
        model_w2v_settings = return_best_model(path=model_settings_path)
        model_path = os.path.join(settings.BASE_DIR, 'news', 'word2vec_models', model_w2v_settings['model_path'])
        self.model_w2v = Word2VecModel(model_w2v_settings, model_path)

        # Load predictive model
        predictive_model_path = os.path.join(settings.BASE_DIR, 'news', 'predictive_models', 'catboost_model.pkl')
        self.predictive_model = load_predictive_model(predictive_model_path)
        
        # load LocalLLM
        self.llm = LocalLLM()

        # load summarizer
        self.summarizer = pipeline("summarization", model="Falconsai/text_summarization")
        
        # load VertexAI
        self.vertex = VertexAI()