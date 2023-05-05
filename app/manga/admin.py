from django.contrib import admin
from .models import Manga, Comment, Rating, Author, Genre
# Register your models here.

admin.site.register(Manga)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Author)
admin.site.register(Genre)