from django.db import models

class Links(models.Model):
  link = models.TextField()
  broken = models.NullBooleanField()
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Movies(models.Model):
  title = models.TextField(unique=True)
  image = models.CharField(max_length=100)
  language = models.CharField(max_length=100, default='English')
  summary = models.TextField()
  links = models.OneToOneField(Links)
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Series(models.Model):#Many-to-One [Each show has many sets of seasons, but season has 1 show]
  title = models.TextField(unique=True)
  image = models.TextField()
  #seasons = models.ManyToManyField(Season)#Table of seasons
  language = models.CharField(max_length=100, default='English')
  number_of_seasons = models.IntegerField()
  summary = models.TextField()
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Season(models.Model):#One-to-One [Each season has one table of episodes]
  title = models.IntegerField(unique=True, default=1)
  series = models.ForeignKey(Series, on_delete=models.CASCADE)
  number_of_episodes = models.IntegerField()
  creationdate = models.DateTimeField(auto_now_add=True)
  updatedate = models.DateTimeField(auto_now=True)

  class Meta():
    app_label = 'fugazzi'


class Episodes(models.Model):
  title = models.IntegerField(unique=True)
  season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
  links = models.OneToOneField(Links)
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
