# Generated by Django 5.0.2 on 2024-06-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_movie_actor_movie_genre_movie_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveIntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')], default=2020),
        ),
    ]
