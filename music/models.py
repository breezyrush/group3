<<<<<<< HEAD
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
=======
from django.db import models
from django.conf import settings
# Create your models here.


class Performers(models.Model):
	performers_genre = models.ForeignKey(Genre)
	performers_name = models.CharField(max_length = 50)

>>>>>>> 16d42800e552f2319e04750c0a413ebc8b1f8269
