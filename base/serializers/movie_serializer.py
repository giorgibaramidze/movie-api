from rest_framework import serializers
from ..models import Movie, Country, Director, Genre, Comment
from .actor_serializer import ActorSerializer


class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = "__all__"
        
    def get_reply(self, obj):
        return CommentSerializer(obj.replies.all(), many=True).data
        
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        
        
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"
        

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"



# ------------------------------- movie serializers----------------------- 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "type", "year", "imdb", "banner"]      
    
    
class BaseMovieSerializer(serializers.Serializer):
    country = CountrySerializer(many=True)
    director = DirectorSerializer(many=True)
    genre = GenreSerializer(many=True)
    actor = ActorSerializer(many=True)
    comment = serializers.SerializerMethodField()

class MovieDetailsSerializer(serializers.ModelSerializer, BaseMovieSerializer):
    class Meta:
        model = Movie
        exclude = ['user']
    
    def get_comment(self, obj):
        return CommentSerializer(obj.movie_comment.filter(reply__isnull=True), many=True).data


class MovieListSerializer(serializers.ModelSerializer, BaseMovieSerializer):
    comment = None
    class Meta:
        model = Movie
        exclude = ['user']