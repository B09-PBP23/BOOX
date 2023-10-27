from django.db import models

from landing_page.models import Books

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
#     upvote_number = models.PositiveIntegerField(default=0, name="upvote_number")

# class ReadersFavorite(models.Model):
#     upvote_number = models.PositiveIntegerField(default=0)
#     books = models.ForeignKey(Books, on_delete=models.CASCADE)