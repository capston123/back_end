from django.db import models
from datetime import date

# Create your models here.


class News(models.Model):
    url = models.TextField()
    image = models.TextField()
    title = models.CharField(max_length=200)
    newspaper = models.CharField(max_length=30)
    category = models.TextField()
    date = models.TextField(default=date.today())
