from django.forms import ModelForm
<<<<<<< HEAD
<<<<<<< HEAD
from django import forms
from .models import *
from django.utils.safestring import mark_safe
=======
from .models import *
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
=======
from .models import *
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394

class FAQForm(ModelForm):
    class Meta:
        model = FAQ
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ['category', 'question', 'is_public']

    widgets = {
        'is_public': forms.CheckboxInput(attrs={'class': 'checkbox'})
    }
=======
        fields = ['category', 'question', 'is_public']
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
=======
        fields = ['category', 'question', 'is_public']
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
