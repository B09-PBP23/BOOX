from django.forms import ModelForm
from .models import *

class FAQForm(ModelForm):
    class Meta:
        model = FAQ
        fields = ['category', 'question', 'is_public']