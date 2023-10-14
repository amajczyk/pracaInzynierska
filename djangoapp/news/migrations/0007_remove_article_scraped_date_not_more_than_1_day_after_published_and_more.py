# Generated by Django 4.2.6 on 2023-10-14 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0006_article_scraped_date_not_more_than_1_day_after_published"),
    ]

    operations = [
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
    ]