# Generated by Django 4.2.6 on 2023-10-14 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "news",
            "0007_remove_article_scraped_date_not_more_than_1_day_after_published_and_more",
        ),
    ]

    operations = [
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
    ]
