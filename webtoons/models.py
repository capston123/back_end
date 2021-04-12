from django.db import models
from django.utils import timezone
# Create your models here.


class Daum(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    image = models.TextField()
    category = models.TextField()
    date = models.TextField(default=timezone.localtime())


class Naver(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    image = models.TextField()
    category = models.TextField()
    date = models.TextField(default=timezone.localtime())
