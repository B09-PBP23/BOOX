from django.forms import ModelForm
from landing_page.models import BookReview

class ReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = ["review", "rating"]
        