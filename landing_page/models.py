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
    total_upvote = models.PositiveIntegerField(default=0)


class BookReview(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, name="book")
    user = models.ForeignKey(User, on_delete=models.CASCADE, name="user")
    review = models.TextField(null=True, blank=True, name="review")
    rating = models.PositiveIntegerField(default=0, name="rating")
    created_at = models.DateTimeField(auto_now_add=True, name="created_at")