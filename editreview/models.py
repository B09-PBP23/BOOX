from django.db import models
from django.contrib.auth.models import User
from landing_page.models import *

# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, name="book")
    user = models.ForeignKey(User, on_delete=models.CASCADE, name="user")
    review = models.TextField(null=True, blank=True, name="review")
    rating = models.PositiveIntegerField(default=0, name="rating")
    created_at = models.DateTimeField(auto_now_add=True, name="created_at")