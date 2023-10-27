from django.db import models
class Books(models.Model):
    title = models.TextField(null=True, blank=True, name="Book-Title")
    author = models.TextField(null=True, blank=True, name="Book-Author")
    year = models.PositiveIntegerField(null=True, blank=True, name="Year-Of-Publication")
    publisher = models.TextField(null=True, blank=True, name="Publisher")
    image_url_s = models.URLField(null=True, blank=True, name="Image-URL-S")
    image_url_m = models.URLField(null=True, blank=True, name="Image-URL-M")
    image_url_l = models.URLField(null=True, blank=True, name="Image-URL-L")

class reviews(models.Model):
    review_text= models.TextField()
    rating = models.PositiveIntegerField(default=0)
    date_added = models.DateField(auto_now_add=True, name="date_added")
# Create your models here.
