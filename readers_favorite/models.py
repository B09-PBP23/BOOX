from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from landing_page.models import Books 

class ReadersFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_contribution = models.IntegerField(default=0)

class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_comment = models.CharField(default="enter comment (max 100)", max_length=100)
    timestamp = models.DateTimeField(default=timezone.now) 
