from django.shortcuts import render
from rest_framework import generics
from .models import Movie, Actor
from .serializers.movie_serializer import MovieSerializer, MovieDetailsSerializer, MovieListSerializer
from .serializers.actor_serializer import ActorSerializer, ActorDetailsSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter
from rest_framework import filters

# ----------------------movie views---------------------------
class MainListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def list(self, request):
        movies = self.queryset.filter(type="movie")[:16]
        serials = self.queryset.filter(type="serial")[:16]
        trailers = self.queryset.filter(type="trailer")[:16]
        actors = Actor.objects.order_by('-id')[:12]
        
        movie_serializer = MovieSerializer(movies, many=True)
        serial_serializer = MovieSerializer(serials, many=True)
        trailer_serializer = MovieSerializer(trailers, many=True)
        actor_serializer = ActorSerializer(actors, many=True)
        
        
        return Response({
            'movies':movie_serializer.data, 
            'serials':serial_serializer.data,
            'trailers': trailer_serializer.data,
            'actors': actor_serializer.data
            })



class MovieDetailsView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailsSerializer
    
    
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MovieFilter
    ordering_fields = ['year', 'imdb']
    
    
# ----------------------actor views------------


class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    

class ActorDetailsView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class =  ActorDetailsSerializer