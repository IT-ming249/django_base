# Generated by Django 5.0.3 on 2025-03-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_tag_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
