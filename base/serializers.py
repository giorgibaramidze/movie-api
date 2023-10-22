from rest_framework import serializers
from .models import Movie, Actor, Country, Director, Genre, Comment

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
        
        
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"



class MovieSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    director = DirectorSerializer(many=True)
    genre = GenreSerializer(many=True)
    actor = ActorSerializer(many=True)
    comment = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"        

    def get_comment(self, obj):
        return CommentSerializer(obj.movie_comment.filter(reply__isnull=True), many=True).data
