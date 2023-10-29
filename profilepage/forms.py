from django import forms
from profilepage.models import Profile
from landing_page.models import Books

class UserProfileForm(forms.ModelForm):
    favorite_books = forms.ModelChoiceField(
        label="Favorite Books",
        queryset=Books.objects.values_list('title', flat=True),
        empty_label="Select a book",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        to_field_name="title"
    )
    favorite_author = forms.ModelChoiceField(
        label="Favorite Author",
        queryset=Books.objects.values_list('author', flat=True),
        empty_label="Select an author",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        to_field_name="author"
    )

    class Meta:
        model = Profile
        fields = ['name', 'profile_picture', 'description', 'favorite_books', 'favorite_author']
