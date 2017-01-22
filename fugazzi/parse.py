#Obsolete
from fugazzi.objects import Movie, Show, Description, Links, Season, Episode


def modelToMovie(modelList):
    try:
        models = modelList #Takes Model
        content_type = Movie #Content type
        object_list = []

        for o in models:
            descr =  Description(o.title, o.image, o.language, o.summary)
            link = Links(o.links.link, o.links.link)
            meta = Meta(o.creationdate, o.updatedate)
            object_list.append(content_type(o.id, descr, link, meta)) #Load Object

        return object_list

    except Exception as e:
        print '%s (%s)' % (e.message, type(e))



def modelToShow(modelList):
    try:
        models = modelList #Takes Model
        content_type = Show #Content type
        object_list = []

        for o in models:
            descr =  Description(o.title, o.image, o.language, o.summary)
            links = Links(o.season.episodes.links.link, o.season.episodes.links.link)#links from links tablle within
            episodes = Episodes(o.season.episodes.id, links)#Should be a list
            seasons = Season(o.season.id, episodes)
            meta = Meta(o.creationdate, o.updatedate)
            show = Show(o.id, descr, seasons, meta)
            object_list.append(show)#Load Object

        return object_list

    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
