# Generated by Django 5.0.2 on 2024-10-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbaproj', '0003_blogpost_feature_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
