from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    
class Bookmarked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    bookmarked_at = models.DateTimeField(auto_now_add=True)
