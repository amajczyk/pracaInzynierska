# Generated by Django 4.2.6 on 2023-10-22 13:58

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    replaces = [
        ("news", "0001_initial"),
        ("news", "0002_remove_article_clickbait_and_more"),
        ("news", "0003_rename_content_article_content_summary"),
        ("news", "0004_article_valid_decision_nlp_and_more"),
        ("news", "0005_alter_article_author_alter_article_pub_date_and_more"),
        ("news", "0006_article_scraped_date_not_more_than_1_day_after_published"),
        (
            "news",
            "0007_remove_article_scraped_date_not_more_than_1_day_after_published_and_more",
        ),
        ("news", "0008_remove_article_published_date_not_later_than_tomorrow_and_more"),
        ("news", "0009_remove_article_published_date_not_later_than_tomorrow_and_more"),
        ("news", "0010_remove_article_published_date_not_later_than_tomorrow_and_more"),
        ("news", "0011_remove_article_published_date_not_later_than_tomorrow_and_more"),
        ("news", "0012_remove_article_published_date_not_later_than_tomorrow_and_more"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content_summary", models.TextField()),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("author", models.CharField(max_length=50)),
                ("url_from", models.CharField(default="", max_length=200)),
                ("clickbait_decision_LLM", models.SmallIntegerField(default=-1)),
                ("clickbait_decision_NLP", models.SmallIntegerField(default=-1)),
                ("clickbait_decision_final", models.SmallIntegerField(default=-1)),
                (
                    "scraped_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("source_site", models.CharField(default="UNKNOWN", max_length=50)),
            ],
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(("clickbait_decision_NLP__in", [-1, 0, 1])),
                name="valid_decision_NLP",
            ),
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(("clickbait_decision_LLM__in", [-1, 0, 1])),
                name="valid_decision_LLM",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name="article",
            name="pub_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="source_site",
            field=models.CharField(default="UNKNOWN", max_length=64),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="article",
            name="url_from",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("pub_date__isnull", True),
                    (
                        "pub_date__lte",
                        datetime.datetime(
                            2023,
                            10,
                            14,
                            18,
                            46,
                            6,
                            396604,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                    _connector="OR",
                ),
                name="scraped_date_not_more_than_1_day_after_published",
            ),
        ),
        migrations.RemoveConstraint(
            model_name="article",
            name="scraped_date_not_more_than_1_day_after_published",
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("pub_date__isnull", True),
                    (
                        "pub_date__lte",
                        datetime.datetime(
                            2023,
                            10,
                            15,
                            18,
                            48,
                            34,
                            822364,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                    _connector="OR",
                ),
                name="published_date_not_later_than_tomorrow",
            ),
        ),
        migrations.RemoveConstraint(
            model_name="article",
            name="published_date_not_later_than_tomorrow",
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("pub_date__isnull", True),
                    (
                        "pub_date__lte",
                        datetime.datetime(
                            2023,
                            10,
                            15,
                            18,
                            56,
                            51,
                            656826,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                    _connector="OR",
                ),
                name="published_date_not_later_than_tomorrow",
            ),
        ),
        migrations.RemoveConstraint(
            model_name="article",
            name="published_date_not_later_than_tomorrow",
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("pub_date__isnull", True),
                    (
                        "pub_date__lte",
                        datetime.datetime(
                            2023,
                            10,
                            15,
                            18,
                            58,
                            59,
                            49006,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                    _connector="OR",
                ),
                name="published_date_not_later_than_tomorrow",
            ),
        ),
        migrations.RemoveConstraint(
            model_name="article",
            name="published_date_not_later_than_tomorrow",
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("pub_date__isnull", True),
                    (
                        "pub_date__lte",
                        datetime.datetime(
                            2023,
                            10,
                            15,
                            19,
                            8,
                            33,
                            490618,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                    _connector="OR",
                ),
                name="published_date_not_later_than_tomorrow",
            ),
        ),
        migrations.RemoveConstraint(
            model_name="article",
            name="published_date_not_later_than_tomorrow",
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("pub_date__isnull", True),
                    (
                        "pub_date__lte",
                        datetime.datetime(
                            2023,
                            10,
                            15,
                            19,
                            12,
                            16,
                            384287,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                    _connector="OR",
                ),
                name="published_date_not_later_than_tomorrow",
            ),
        ),
        migrations.RemoveConstraint(
            model_name="article",
            name="published_date_not_later_than_tomorrow",
        ),
        migrations.AddConstraint(
            model_name="article",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("pub_date__isnull", True),
                    (
                        "pub_date__lte",
                        datetime.datetime(
                            2023,
                            10,
                            23,
                            13,
                            56,
                            46,
                            739776,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                    _connector="OR",
                ),
                name="published_date_not_later_than_tomorrow",
            ),
        ),
    ]
