# Generated by Django 3.0.8 on 2020-08-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='first-blog'),
        ),
    ]
