from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.TextField()
    name = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now_add=True)
    description = models.TextField()