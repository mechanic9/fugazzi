from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from fugazzi.models import Movies, Series, Upcoming, Popular, Season, Episodes
from fugazzi.actions import getIndex, getHomeContent, getMovContent, getShowContent

#Items on a page
pg_limit = 18

#Links
movies = '/movies'
shows = '/shows'
home = '/'
img = '/img/'
stat_home = 'fugazzi/'


def homepage(request):
    html = 'Group_Pages/homepage.html'
    whole_db = Movies.objects.all()#Query All

    #Page vars for template
    page_arg = 'page'#Arg for get
    page_q = '?'+page_arg+'=' #Page query without value
    total_pgs = len(whole_db)/pg_limit #Total no of pages
    if(len(whole_db) % pg_limit != 0):
        total_pgs = total_pgs+1 #Total no of pages
    page_list = []
    for i in xrange(1, total_pgs+1):
        page_list.append(i)

    #Handling Page Arg
    page = int(request.GET.get(page_arg, 1))
    if(page < 1):
        page = 1
    if(page >= total_pgs):
        page = total_pgs

    #Getting Content
    movs = getHomeContent(page, pg_limit)
    topcontent = []

    #Vars for watch url
    table = '/movies'
    url_stat = '/watch'
    title_pre = '/'

    #DB dict to template list
    for m in movs:
        topcontent.append([table+title_pre+m.title+url_stat, m.title, img+m.image, m.title ,m.language, 'm.releaseyear'])

    #topcontent = [[table+title_pre+m.title+url_stat, m.title, img+'x.jpeg', m.title ,m.language, 'm.releaseyear']]*20
    #test = topcontent
    context = {'movies':movies, 'shows':shows,
'home':home, 'stat':stat_home, 'top':topcontent, 'pg_q':page_q, 'page_list':page_list, 'page':page}
    return render(request, html, context)

def groupmovies(request):
#For after cards are emailed
    html = 'Group_Pages/movies.html'
    whole_db = Movies.objects.all()#Query All Movies

    #Page vars for template
    page_arg = 'page'#Arg for get
    page_q = '?'+page_arg+'=' #Page query without value
    total_pgs = len(whole_db)/pg_limit #Total no of pages
    if(len(whole_db) % pg_limit != 0):
        total_pgs = total_pgs+1 #Total no of pages
    page_list = []
    for i in xrange(1, total_pgs+1):
        page_list.append(i)

    #Handling Page Arg
    page = int(request.GET.get(page_arg, 1))
    if(page < 1):
        page = 1
    if(page >= total_pgs):
        page = total_pgs

    #Getting Content
    movs = getMovContent(page, pg_limit)
    topcontent = []

    #Vars for watch url
    table = '/movies'
    url_stat = '/watch'
    title_pre = '/'

    #DB dict to template list
    for m in movs:
        topcontent.append([table+title_pre+m.title+url_stat, m.title, img+m.image, m.title ,m.language, 'm.releaseyear'])

    #topcontent = []
    #test = topcontent
    context = {'movies':movies, 'shows':shows,
'home':home, 'stat':stat_home, 'top':topcontent, 'pg_q':page_q, 'page_list':page_list, 'page':page}
    return render(request, html, context)

def groupshows(request):
    html = 'Group_Pages/tvshows.html'
    whole_db = Series.objects.all()#Query All Shows

    #Page vars for template
    page_arg = 'page'#Arg for get
    page_q = '?'+page_arg+'=' #Page query without value
    total_pgs = len(whole_db)/pg_limit
    if(len(whole_db) % pg_limit != 0):
        total_pgs = total_pgs+1 #Total no of pages
    page_list = []
    for i in xrange(1, total_pgs+1):
        page_list.append(i)

    #Handling Page Arg
    page = int(request.GET.get(page_arg, 1))
    if(page < 1):
        page = 1
    if(page >= total_pgs):
        page = total_pgs

    #Getting Content
    series = getShowContent(page, pg_limit)
    topcontent = []

    #Vars for view url
    table = '/shows'
    #url_stat = '/view'
    title_pre = '/'
    glue = '&'
    s_pre = '?season='
    ep_pre = '?episode='

    #DB dict to template list
    for m in series:
        url = table+title_pre+m.title
        topcontent.append([url, m.title, img+m.image, m.title ,m.language, 'm.releaseyear'])

    #topcontent = []
    #test = topcontent
    context = {'movies':movies, 'shows':shows,
'home':home, 'stat':stat_home, 'top':topcontent, 'pg_q':page_q, 'page_list':page_list, 'page':page}
    return render(request, html, context)

def watch(request, tab, title):
    html = 'View_Pages/watch.html'

    #Handling Args
    table = tab
    #title = str(request.GET.get('title'))
    season_no = int(request.GET.get('season', 1))
    episode_no = int(request.GET.get('episode', 1))

    #Handling Query
    if(table == 'shows'):
        entry = Series.objects.get(title=title)
        season = Season.objects.get(series=entry, title=season_no)
        episode = Episodes.objects.get(season=season, title=episode_no)
        link = episode.links.link
    elif(table == 'movies'):
        entry = Movies.objects.get(title=title)
        link = entry.links.link

    info = [img+entry.image, entry.title, link]

    context = {'movies':movies, 'shows':shows,
'home':home, 'stat':stat_home, 'info':info}
    return render(request, html, context)

def viewshows(request, title):
    html = 'View_Pages/show_view.html'

    #Queries
    entry = Series.objects.get(title=title)
    seasons = Season.objects.filter(series=entry)
    episodes = []
    season_list = []
    ep_list = []

    #Vars for view url
    table = '/shows'
    url_stat = '/watch'
    title_pre = '/'
    glue = '&'
    s_pre = '?season='
    ep_pre = '?episode='
    url = table+title_pre+title+url_stat #Url with title

    for s in xrange(len(seasons)):
        episodes.append(Episodes.objects.filter(season=seasons[s]))#List of querysets
        season_list.append([seasons[s].title, []])
        #ep_list.append([])
        for e in episodes[s]:
            link = url+s_pre+str(seasons[s].title)+glue+ep_pre+str(e.title) #Url with season and episode
            season_list[s][1].append([e.title, link])

    info = [img+entry.image, entry.title]

    context = {'movies':movies, 'shows':shows,
'home':home, 'stat':stat_home, 'info':info,'season_list':season_list, 'ep_list':ep_list}
    return render(request, html, context)
