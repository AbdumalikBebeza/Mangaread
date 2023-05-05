from django.urls import path
from .views import *

list_create = {
    'get': 'list',
    'post': 'create'}

update_retrieve_destroy = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'}

urlpatterns = [
    path('manga/', MangaListViewSet.as_view(list_create)),
    path('manga/<int:pk>/', MangaListViewSet.as_view(update_retrieve_destroy)),
    path('authors/', AuthorListViewSet.as_view(list_create)),
    path('authors/<int:pk>/', AuthorListViewSet.as_view(update_retrieve_destroy)),
    path('comments/', CommentListViewSet.as_view(list_create)),
    path('comments/<int:pk>', CommentListViewSet.as_view(update_retrieve_destroy)),
    path('genres/', GenreListViewSet.as_view(list_create)),
    path('genres/<int:pk>', GenreListViewSet.as_view(update_retrieve_destroy)),
]
