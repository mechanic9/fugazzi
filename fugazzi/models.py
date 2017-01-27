from django.db import models
from django.utils import timezone
import datetime

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()

class Links(models.Model):
  link = models.TextField()
  broken = models.NullBooleanField()
  creationdate = models.DateTimeField(default=timezone.now, editable=False)
  updatedate = AutoDateTimeField(default=timezone.now, editable=False)

  class Meta():
    app_label = 'fugazzi'


class Movies(models.Model):
  title = models.TextField(unique=True)
  image = models.CharField(max_length=100)
  language = models.CharField(max_length=100, default='English')
  summary = models.TextField()
  links = models.OneToOneField(Links)
  creationdate = models.DateTimeField(default=timezone.now, editable=False)
  updatedate = AutoDateTimeField(default=timezone.now, editable=False)

  class Meta():
    app_label = 'fugazzi'


class Series(models.Model):#Many-to-One [Each show has many sets of seasons, but season has 1 show]
  title = models.TextField(unique=True)
  image = models.TextField()
  #seasons = models.ManyToManyField(Season)#Table of seasons
  language = models.TextField(max_length=100, null=True, default='English')
  summary = models.TextField()
  creationdate = models.DateTimeField(default=timezone.now, editable=False)
  updatedate = AutoDateTimeField(default=timezone.now, editable=False)

  class Meta():
    app_label = 'fugazzi'


class Season(models.Model):#One-to-One [Each season has one table of episodes]
  title = models.IntegerField(unique=True, default=1)
  series = models.ForeignKey(Series, on_delete=models.CASCADE)
  creationdate = models.DateTimeField(default=timezone.now, editable=False)
  updatedate = AutoDateTimeField(default=timezone.now, editable=False)

  class Meta():
    app_label = 'fugazzi'


class Episodes(models.Model):
  title = models.IntegerField(unique=True)
  season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
  links = models.OneToOneField(Links)
  creationdate = models.DateTimeField(default=timezone.now, editable=False)
  updatedate = AutoDateTimeField(default=timezone.now, editable=False)

  class Meta():
    app_label = 'fugazzi'


class Popular(models.Model):#One-to-One [Each tables has one table of movies and series]
  movies = models.OneToOneField(Movies)
  series = models.OneToOneField(Series)
  creationdate = models.DateTimeField(default=timezone.now, editable=False)
  updatedate = AutoDateTimeField(default=timezone.now, editable=False)


  class Meta():
    app_label = 'fugazzi'


class Upcoming(models.Model):#One-to-One [Each tables has one table of movies and series]
  movies = models.OneToOneField(Movies)
  series = models.OneToOneField(Series)
  creationdate = models.DateTimeField(default=timezone.now, editable=False)
  updatedate = AutoDateTimeField(default=timezone.now, editable=False)

  class Meta():
    app_label = 'fugazzi'
