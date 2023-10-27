from django.forms import ModelForm
from main.models import BookReview

class ReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = ["review", "rating"]
        