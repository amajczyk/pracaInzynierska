# Generated by Django 4.2.6 on 2024-01-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0005_article_clickbait_probability_llm_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="subcategory",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
