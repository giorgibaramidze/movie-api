from django.contrib import admin
from .models import Movie, Actor, Genre

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
