from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
<<<<<<< HEAD
from django.utils import timezone
=======
from django.utils import timezone  # Import the timezone module
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
=======
from django.utils import timezone  # Import the timezone module
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394

class ReadersFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_contribution = models.IntegerField(default=0)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_comment = models.CharField(default="enter comment (max 100)", max_length=100)
<<<<<<< HEAD
<<<<<<< HEAD
    timestamp = models.DateTimeField(default=timezone.now) 
=======
    timestamp = models.DateTimeField(default=timezone.now) 
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
=======
    timestamp = models.DateTimeField(default=timezone.now) 
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
