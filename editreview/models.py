

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from landing_page.models import Books, BookReview

# class Review(models.Model):
#     book = models.ForeignKey(Books, on_delete=models.CASCADE)
#     reviewbuku = models.TextField(null=True, blank=True)
#     rate = models.PositiveIntegerField(default=0)
#     gambar_url_m = models.URLField(null=True, blank=True)
