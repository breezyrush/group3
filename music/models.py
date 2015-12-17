from django.db import models
from django.conf import settings
# Create your models here.


class Performers(models.Model):
	performers_genre = models.ForeignKey(Genre)
	performers_name = models.CharField(max_length = 50)

