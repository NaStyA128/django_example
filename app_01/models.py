from django.db import models
from django.conf import settings


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

# Create your models here.
