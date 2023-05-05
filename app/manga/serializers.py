from rest_framework import serializers
from manga.models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id text manga'.split()


class AuthorSerializer(serializers.ModelSerializer):
    manga_count = serializers.SerializerMethodField

    class Meta:
        model = Author
        fields = 'id fullname manga_count'.split()

    def get_manga_count(self, author):
        return author.manga_count


class MangaSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField
    average_rate = serializers.SerializerMethodField
    genre_name = serializers.SerializerMethodField
    comments_text = serializers.SerializerMethodField

    class Meta:
        model = Manga
        fields = 'id ru_title eng_title description publishing_house issue_year ' \
                 'chapter type author_name average_rate image genre_name' \
                 ' comments_text'.split()

    def get_author_name(self, manga):
        return manga.author_name

    def get_average_rate(self, manga):
        return manga.average_rate

    def get_genre_name(self, manga):
        return manga.genre_name

    def get_comments_text(self, manga):
        return manga.comments_text


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = 'id rate manga'.split()


class GenreSerializer(serializers.ModelSerializer):
    manga_count = serializers.SerializerMethodField

    class Meta:
        model = Genre
        fields = 'id name manga_count'.split()

    def get_manga_count(self, genre):
        return genre.manga_count


class FilteredGenreMangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = 'image ru_title eng_title chapter type genre author publishing_house'.split()
