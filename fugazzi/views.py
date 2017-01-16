from django.shortcuts import render
from django.contrib.auth.models import User
from fugazzi.models import Movies, Series, Upcoming, Popular

#Links
movies = '/movies'
shows = '/shows'
home = '/home'

def homepage(request):
#order page as well
    movies = Movies.objects.all()#Query All
    html = 'Group_Pages/homepage.html'
    toplimit = 15
    leftlimit = 11
    topcontent = [[]]
    #Loop
    for m in movies:
        topcontent.append([m.viewlink, m.title, m.img, m.title,m.lang, m.releaseyear])
    latest = [["/alternative-music/","/thefence/Images/index.jpeg",m.title,"Alternative"]]*17
    upcoming = [["/alternative-music/","/thefence/Images/index.jpeg","Tester","Alternative"]]

    context = {'movies':movies, 'shows':shows,
'home':home, 'top':topcontent, 'latest':latest, 'upcoming':upcoming}
    return render(request, html, context)

def groupmovies(request):
#For after cards are emailed
    html = 'Group_Pages/movies.html'
    pglimit = 15
    topcontent = [["http://freealbums.org/1094-seyed-engel-mit-der-ak-2016.html","Drake Is Bae","/thefence/Images/x.jpeg","Drake - Views (Deluxe Edition) (2016)","English","2016"],["http://freealbums.org/1094-seyed-engel-mit-der-ak-2016.html","Drake Is Bae","/thefence/Images/x.jpeg","Drake - Views (Deluxe Edition) (2018)","English","2018"],["http://freealbums.org/1094-seyed-engel-mit-der-ak-2016.html","Drake Is Bae","/thefence/Images/x.jpeg","Drake - Views (Deluxe Edition) (2019)","English","2019"]]
    latest = [["/alternative-music/","/thefence/Images/index.jpeg","Tester","Alternative"]]
    upcoming = [["/alternative-music/","/thefence/Images/index.jpeg","Tester","Alternative"]]
    context = {'movies':movies, 'shows':shows,
'home':home, 'topcontent':topcontent,'latest':latest,'upcoming':upcoming}
    return render(request, html, context)

def groupshows(request):
    html = 'Group_Pages/tvshows.html'
    topcontent = []
    latest = []
    upcoming = []
    context = {'movies':movies, 'shows':shows,
'home':home, 'topcontent':topcontent,'latest':latest,'upcoming':upcoming}
    return render(request, html, context)

def viewmovies(request):
    html = 'View_Pages/movie-view.html'
    info = []
    beef= []
    latest=[]
    upcoming=[]
    context = {'movies':movies, 'shows':shows,
'home':home, 'info':info,'beef':beef, 'latest':latest,'upcoming':upcoming}
    return render(request, html, context)

def viewshows(request):
    html = 'View_Pages/tvshow-view.html'
    info=[]
    beef=[]
    latest=[]
    upcoming=[]
    context = {'movies':movies, 'shows':shows,
'home':home, 'info':info,'beef':beef, 'latest':latest,'upcoming':upcoming}
    return render(request, html, context)

def viewepisodes(request):
    html = 'View_Pages/episode-view.html'
    info=[]
    beef=[]
    latest=[]
    upcoming=[]
    context = {'movies':movies, 'shows':shows,
'home':home, 'info':info,'beef':beef, 'latest':latest,'upcoming':upcoming}
    return render(request, html, context)
