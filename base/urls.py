from base import views
from django.urls import path


urlpatterns = [
    path('main/', views.MainListView.as_view(), name="main"),
    path('movie/<uuid:pk>/', views.MovieDetailsView.as_view(), name="movie-details"),
    path('movie/', views.MovieListView.as_view(), name='movie-list')
]
