# Generated by Django 2.2.28 on 2025-02-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
