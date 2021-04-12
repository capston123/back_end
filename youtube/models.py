from django.db import models
from django.utils import timezone

# Create your models here.
class Youtube(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    image = models.TextField()
    category = models.TextField()
    channel = models.TextField()
    date = models.DateTimeField(auto_now_add=True)