from django.db import models
from datetime import date

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=100)
    newspaper = models.CharField(max_length=30)
    url = models.TextField()
    image = models.TextField()
    category = models.TextField()
    date = models.TextField(default=date.today())