from rest_framework import serializers
from .models import Movie
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField

class MovieSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country = CountryField()
    class Meta:
        model = Movie
        fields = '__all__'