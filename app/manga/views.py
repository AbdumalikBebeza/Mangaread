from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from .paginations import GenrePagination,MangaLimitOffsetPagination
from .filters import MangaFilter
# Create your views here.


class MangaListViewSet(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    pagination_class = MangaLimitOffsetPagination
    filterset_class = MangaFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['ru_title', 'eng_title']


class AuthorListViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CommentListViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GenreListViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = GenrePagination


class FilteredGenreMangaAPIView(ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = FilteredGenreMangaSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class.data, status=status.HTTP_200_OK)

