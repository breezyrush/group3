# -*- coding: utf-8 -*-
from __future__ import unicode_literals

<<<<<<< HEAD
from django.db import models, migrations
=======
from django.db import migrations, models
>>>>>>> 16d42800e552f2319e04750c0a413ebc8b1f8269


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
<<<<<<< HEAD
                ('genre_name', models.CharField(max_length=120)),
=======
                ('genre_name', models.CharField(max_length=200)),
>>>>>>> 16d42800e552f2319e04750c0a413ebc8b1f8269
            ],
        ),
        migrations.CreateModel(
            name='Performers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
<<<<<<< HEAD
                ('performers_name', models.CharField(max_length=120)),
=======
                ('performers_name', models.CharField(max_length=50)),
                ('performers_genre', models.ForeignKey(to='music.Genre')),
>>>>>>> 16d42800e552f2319e04750c0a413ebc8b1f8269
            ],
        ),
    ]
