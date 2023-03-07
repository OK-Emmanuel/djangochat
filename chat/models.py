from django.db import models
from datetime import datetime
# Create your models here.
# Two classes of models created: one for the user and the other for chat backup
class Room(models.Model):
    name = models.CharField(max_length=150)

class Message(models.Model):
    message = models.TextField(100000)
    date = models.DateTimeField(default= datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=500)
  


