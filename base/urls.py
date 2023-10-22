from base import views
from django.urls import path


urlpatterns = [
    path('movies/', views.MovieListView.as_view(), name="movie-list")
]
