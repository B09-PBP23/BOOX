from django import forms
from django.forms import ModelForm
from editreview.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["review", "rating"]
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
        labels = {
            'review': 'Edit Review',
            'rating': 'Edit Rating (1-5)',
        }