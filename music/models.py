from __future__ import unicode_literals
from django.db import IntegrityError
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Genre(models.Model):
    genre_name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.genre_name



class Performers(models.Model):
    performers_name = models.CharField(max_length=120)
