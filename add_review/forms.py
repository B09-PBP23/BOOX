from django.forms import ModelForm
from add_review.models import * 
from editreview.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["review", "rating"]