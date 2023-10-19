from django.db import models
import uuid
from django_countries.fields import CountryField
from accounts.models import Account
import datetime

YEAR_CHOICES = [(r, r) for r in range(1950, datetime.date.today().year + 2)]

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
    
    class Meta:
        db_table = "actor"
        ordering = ['full_name']
        
    def __str__(self):
        return self.full_name


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='author', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    country = CountryField(multiple=True)
    genre = models.ManyToManyField(Genre)
    
    class Meta:
        db_table = "movie"
        ordering = ['-id']
        
    def __str__(self):
        return self.title
    
