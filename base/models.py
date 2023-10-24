from django.db import models
import uuid
from accounts.models import Account
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


YEAR_CHOICES = [(r, r) for r in range(1950, datetime.date.today().year + 2)]
TYPE_CHOICES = [
    ('movie', 'movie'),
    ('trailer', 'trailer'),
    ('serial', 'serial')
]

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    
    class Meta:
        db_table = "genre"
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    
class Actor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=70)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='images/actors')
    
    class Meta:
        db_table = "actor"
        ordering = ['full_name']
        
    def __str__(self):
        return self.full_name


class Director(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/director')
    date_of_birth = models.DateField()

    class Meta:
        db_table = "director"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    
    class Meta:
        db_table = "country"
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='author', blank=True, null=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=60, choices=TYPE_CHOICES, default='movie')
    banner = models.ImageField(upload_to='images/movies')
    description = models.TextField(max_length=255)
    imdb = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    genre = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)
    
    class Meta:
        db_table = "movie"
        ordering = ['-id']
        
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_comment')
    reply = models.ForeignKey('Comment', blank=True, null=True, related_name='replies', on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"
        ordering = ['id']
        
    def __str__(self):
        return self.comment
