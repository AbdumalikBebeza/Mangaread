from django_filters import rest_framework as filters
from .models import Manga


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MangaFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__name', lookup_expr='in')
    issue_year = filters.RangeFilter()

    class Meta:
        model = Manga
        fields = 'issue_year genre'.split()
