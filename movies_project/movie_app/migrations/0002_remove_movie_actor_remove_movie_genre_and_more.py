# Generated by Django 5.0.2 on 2024-06-30 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]