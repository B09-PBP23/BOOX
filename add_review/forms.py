from django.forms import ModelForm
from add_review.models import * 

class ReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = ["review", "rating"]