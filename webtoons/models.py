from django.db import models
from datetime import date
# Create your models here.


class Daum(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    image = models.TextField()
    category = models.TextField()
    date = models.TextField(default=date.today())


class Naver(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    image = models.TextField()
    category = models.TextField()
    date = models.TextField(default=date.today())
