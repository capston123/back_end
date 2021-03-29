from django.db import models
from datetime import date
# Create your models here.
class Youtube(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    image = models.TextField()
    category = models.TextField()
    channel = models.TextField()
    date = models.TextField(default=date.today())