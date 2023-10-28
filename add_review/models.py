from django.db import models
from django.contrib.auth.models import User
from landing_page.models import *

# Create your models here.
# class Books(models.Model):
#     isbn = models.TextField(null=True, blank=True, name="ISBN")
#     title = models.TextField(null=True, blank=True, name="Book-Title")
#     author = models.TextField(null=True, blank=True, name="Book-Author")
#     year = models.PositiveIntegerField(null=True, blank=True, name="Year-Of-Publication")
#     publisher = models.TextField(null=True, blank=True, name="Publisher")
#     image_url_s = models.URLField(null=True, blank=True, name="Image-URL-S")
#     image_url_m = models.URLField(null=True, blank=True, name="Image-URL-M")
#     image_url_l = models.URLField(null=True, blank=True, name="Image-URL-L")
#     total_ratings = models.FloatField(default=0, name="Rating")
#     total_reviews = models.PositiveIntegerField(default=0, name="Reviews")

# class BookReview(models.Model):
#     book = models.ForeignKey(Books, on_delete=models.CASCADE, name="book")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, name="user")
#     review = models.TextField(null=True, blank=True, name="review")
#     rating = models.PositiveIntegerField(default=0, name="rating")
#     created_at = models.DateTimeField(auto_now_add=True, name="created_at")

