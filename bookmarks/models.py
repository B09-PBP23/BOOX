from django.db import models
from django.contrib.auth.models import User
from landing_page.models import Books

class Bookmarked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    bookmarked_at = models.DateTimeField(auto_now_add=True)
