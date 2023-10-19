from django.db import models
import uuid
from django_countries.fields import CountryField
from accounts.models import Account
import datetime

YEAR_CHOICES = [(r, r) for r in range(1950, datetime.date.today().year + 4)]


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='author', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    country = CountryField(multiple=True)
    
