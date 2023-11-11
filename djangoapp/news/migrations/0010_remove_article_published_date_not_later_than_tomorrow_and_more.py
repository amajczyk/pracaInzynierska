# Generated by Django 4.2.6 on 2023-10-14 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0009_remove_article_published_date_not_later_than_tomorrow_and_more"),
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
    ]