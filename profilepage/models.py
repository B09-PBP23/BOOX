from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now_add=True)
    description = models.TextField()