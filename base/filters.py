import django_filters
from .models import Movie


class MovieFilter(django_filters.FilterSet):
    year__gt = django_filters.NumberFilter(field_name='year', lookup_expr='gt')
    year__lt = django_filters.NumberFilter(field_name='year', lookup_expr='lt')
    imdb__gt = django_filters.NumberFilter(field_name='imdb', lookup_expr='gt')
    imdb__lt = django_filters.NumberFilter(field_name='imdb', lookup_expr='lt')
    
    class Meta:
        model = Movie
        fields = ['type', 'year__gt', 'year__lt', 'country', 'imdb__gt', 'imdb__lt', 'genre']