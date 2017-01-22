#obsolete

class Meta:
    def __init__(self, creation, update):
        self.creation = creation
        self.update = update

    #Getters
    def getCreationDate(self):
        return self.creation

    def getUpdateDate(self):
        return self.update

class Description:
    def __init__(self, title, image, language, summary):
        self.title = title
        self.image = image
        self.language = language
        self.summary = summary

    #Getters
    def getTitle(self):
        return self.title

    def getImage(self):
        return self.image

    def getLanguage(self):
        return self.language

    def getSummary(self):
        return self.summary


class Links:
    def __init__(self, watch, download):
        self.watch = watch
        self.download = download

    #Getters
    def getWatchLink(self):
        return self.watch

    def getDownloadLink(self):
        return self.download


class Movie:
    def __init__(self, pk, descr, links, meta):
        self.id = pk;
        self.description = descr
        self.links = links
        self.meta = meta

    #Getters
    def getId(self):
        return self.id

    def getDescription(self):
        return self.description

    def getLinks(self):
        return self.links

    def getMeta(self):
        return self.meta


class Show:
    def __init__(self, pk, descr, seasons, meta):
        self.id = pk;
        self.description = descr
        self.seasons = seasons
        self.meta = meta

    #Getters
    def getId(self):
        return self.id

    def getDescription(self):
        return self.description

    def getSeasons(self):
        return self.season

    def getMeta(self):
        return self.meta


class Season:
    def __init__(self, pk, eplist):
        self.id = pk;
        self.eplist = eplist

    #Getters
    def getId(self):
        return self.id

    def getEpisodes(self):
        return self.eplist


class Episode:
    def __init__(self, pk, links):
        self.id = pk;
        self.links = links

    #Getters
    def getId(self):
        return self.id

    def getLinks(self):
        return self.links
