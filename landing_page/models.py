from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    isbn = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    image_url_s = models.URLField(null=True, blank=True)
    image_url_m = models.URLField(null=True, blank=True)
    image_url_l = models.URLField(null=True, blank=True)
    total_ratings = models.FloatField(default=0)
    total_reviews = models.PositiveIntegerField(default=0)
    

class BookReview(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
class FAQ(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.TextField(null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=True)
