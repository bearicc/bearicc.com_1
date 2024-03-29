from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    post = models.ForeignKey(Post)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True)
    name = models.CharField(max_length=30, default='Guest')
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
