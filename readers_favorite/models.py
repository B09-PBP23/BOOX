from django.db import models
from django.contrib.auth.models import User

class ReadersFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_comment = models.CharField(default="enter comment (max 100)", max_length=100)
    user_contribution = models.IntegerField(default=0)