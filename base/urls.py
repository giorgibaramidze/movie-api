from base import views
from django.urls import path


urlpatterns = [
    path('main/', views.MainListView.as_view(), name="main"),
    path('movie/', views.MovieListView.as_view(), name='movie-list'),
    path('movie/<uuid:pk>/', views.MovieDetailsView.as_view(), name="movie-details"),
    path('actor/', views.ActorListView.as_view(), name='actor-list'),
    path('actor/<uuid:pk>/', views.ActorDetailsView.as_view(), name='actor-details')
]
