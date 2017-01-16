from django.db import models

class Links(models.Model):
  link = models.TextField()
  quality = models.CharField(max_length=20)
  downloadable = models.BooleanField()
  broken = models.NullBooleanField()
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Movies(models.Model):
  title = models.TextField()
  img = models.CharField(max_length=100)
  viewlink = models.CharField(max_length=100)
  lang = models.CharField(max_length=100)
  releaseyear = models.IntegerField()
  #cast = models.OneToOneField(Cast)#Table of cast members
  summary = models.TextField()
  links = models.OneToOneField(Links)
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Episodes(models.Model):
  title = models.TextField()
  viewlink = models.CharField(max_length=100)
  links = models.OneToOneField(Links)
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Series(models.Model):#Many-to-One [Each show has many sets of seasons, but season has 1 show]
  title = models.TextField()
  img = models.TextField()
  viewlink = models.CharField(max_length=100)
  #seasons = models.ManyToManyField(Season)#Table of seasons
  lang = models.CharField(max_length=100)
  numofseasons = models.IntegerField()
  genre = models.CharField(max_length=100)
  summary = models.TextField()
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Season(models.Model):#One-to-One [Each season has one table of episodes]
  num = models.IntegerField()
  series = models.ForeignKey(Series, on_delete=models.CASCADE)
  episodes = models.OneToOneField(Episodes)#Table of episodes
  numofepisodes = models.IntegerField()
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Cast(models.Model):
  name = models.TextField()
  movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Popular(models.Model):#One-to-One [Each tables has one table of movies and series]
  movies = models.OneToOneField(Movies)
  series = models.OneToOneField(Series)
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Upcoming(models.Model):#One-to-One [Each tables has one table of movies and series]
  movies = models.OneToOneField(Movies)
  series = models.OneToOneField(Series)
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'

