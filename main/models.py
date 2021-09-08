from django.contrib.auth.models import User
from django.db import models


# Create your models here.
def upload_to(instance, filename):
    return f'{filename}'


class News(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now=True)
    short_description = models.CharField(max_length=1000)
    full_description = models.TextField()
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title


class LawType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Law(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    law_type = models.ForeignKey(LawType, on_delete=models.SET_NULL, null=True)


class ImageNews(models.Model):
    image = models.ImageField(upload_to=upload_to)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.news.title


class FavouriteNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


PUBLICATION_TYPES = (
    (1, 'Публикации NCO'),
    (2, 'Другие публикации')
)


class Publication(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    file = models.FileField(null=True, blank=True)
    types = models.IntegerField(choices=PUBLICATION_TYPES, default=1)