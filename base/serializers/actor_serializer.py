from rest_framework import serializers
from ..models import Movie, Actor
from . import movie_serializer

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
        
class ActorDetailsSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    class Meta:
        model = Actor
        fields = "__all__"
        
    def get_movies(self, obj):
        return movie_serializer.MovieSerializer(obj.movie_set.all(), many=True).data
        