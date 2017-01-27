from django.contrib import admin
from .models import Movies, Series, Links, Season, Episodes, Popular, Upcoming

admin.site.register(Movies)
admin.site.register(Series)
admin.site.register(Links)
admin.site.register(Season)
admin.site.register(Episodes)
admin.site.register(Popular)
admin.site.register(Upcoming)
