from fugazzi.models import Movies, Series

offset = 1

def getIndex(pageno, pertable):
        if(pageno < 1):
            pageno = 1
        starti = ((pageno - offset)*pertable)#1 less than actual [0=1st]
        endi = starti + pertable# exact [10=10th]
        i = {'start':starti, 'end':endi}

        return i


def getHomeContent(pageno, pertable):
        i = getIndex(pageno, pertable)
        start = i['start']
        end = i['end']
        mov = Movies.objects.all()[start:end]

        return mov


def getMovContent(pageno, pertable):
        i = getIndex(pageno, pertable)
        start = i['start']
        end = i['end']
        mov = Movies.objects.all()[start:end]

        return mov


def getShowContent(pageno, pertable):
        i = getIndex(pageno, pertable)
        start = i['start']
        end = i['end']
        show = Series.objects.all()[start:end]

        return show


def getWatchPage(pk, table):
    if(table == 'movies'):
        c = Movies.objects.get(pk=pk)
    elif(table == 'shows'):
        c = Series.objects.get(pk=pk)
    description = {'title': c.title,'image': c.image, 'summary': c.summary, 'language': c.language}
    page = {'description':[description], 'watchlink':c.links.link, 'downlink':c.links.link}

    return page


def getViewPage(pk):
    c = Series.objects.get(pk=pk)
    page = {'season':['']}

    return page
