from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def manga_count(self):
        return self.manga.all().count()


class Author(models.Model):
    fullname = models.CharField(max_length=150)

    def __str__(self):
        return self.fullname

    @property
    def manga_count(self):
        return self.manga.all().count()




MANGA_TYPE_CHOICES = (
    ('манга', 'манга'),
    ('манхва', 'манхва'),
    ('маньхуа', 'маньхуа'),
    ('комикс', 'комикс'),
    ('комикс', 'комикс'),
)


class Manga(models.Model):
    ru_title = models.CharField(max_length=150)
    eng_title = models.CharField(max_length=100, default='')
    image = models.ImageField(null=True)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='manga')
    publishing_house = models.CharField(max_length=150)
    chapter = models.PositiveIntegerField()
    genre = models.ManyToManyField(Genre, related_name='manga')
    type = models.CharField(max_length=50, choices=MANGA_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    issue_year = models.IntegerField(null=True)

    def __str__(self):
        return self.ru_title

    @property
    def average_rate(self):
        count = int(self.rating.all().count())
        sum_rate = sum([i.rate for i in self.rating.all()])
        return sum_rate / count

    @property
    def comments_text(self):
        return [[i.id, i.text] for i in self.comments.all()]

    @property
    def author_name(self):
        return self.author.fullname

    @property
    def genre_name(self):
        return [i.name for i in self.genre.all()]


class Rating(models.Model):
    rate = models.IntegerField(choices=([i, i * '*'] for i in range(1, 11)), default=1)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='rating')

    def __str__(self):
        return str(self.rate)


class Comment(models.Model):
    text = models.TextField()
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text

    @property
    def manga_title(self):
        return self.manga.ru_title, self.manga.eng_title
