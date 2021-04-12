from django.db import models
from django.utils import timezone

# Create your models here.


class News(models.Model):
    url = models.TextField()
    image = models.TextField()
    name = models.TextField()
    newspaper = models.TextField()
    category = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
