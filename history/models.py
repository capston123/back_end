from django.db import models
from datetime import datetime

# Create your models here.
class History(models.Model):
    user_id = models.TextField()
    category = models.TextField()
    content_number = models.TextField()
    content_class=models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    