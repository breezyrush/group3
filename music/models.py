from django.db import models

from __future__ import unicode_literals
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


#To do: Select Performer - Obtain Performer work records 
# - return performer work records - display all cd's or other works
class Cd_name(models.Model):
	Cd_name = models.CharField(max_length=200)
	Cd_price = models.CharField(max_length=200)
	Performer_name = models.ForeignKey(Artist)

	def __unicode__(self):
        return self.Performers_name



