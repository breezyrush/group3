from django.db import models

# Create your models here.

class Songs(models.Models):
	song_name = models.CharField(max_length=50)
	cdid = models.ForeignKey(Cd)

	def __unicode__(self):
		return self.song_name

class Cart(models.Models)
    cdid = models.ForeignKey(Cd)
    purdate = models.DateTimeField(default = timezone.now())