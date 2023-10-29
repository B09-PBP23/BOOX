from django.forms import ModelForm
from django import forms
from .models import *
from django.utils.safestring import mark_safe

class FAQForm(ModelForm):
    class Meta:
        model = FAQ
        fields = ['category', 'question', 'is_public']

    widgets = {
        'is_public': forms.CheckboxInput(attrs={'class': 'checkbox'})
    }