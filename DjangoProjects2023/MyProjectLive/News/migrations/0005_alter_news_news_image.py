# Generated by Django 4.1.5 on 2023-10-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_news_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='newimg/'),
        ),
    ]
