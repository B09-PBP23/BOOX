from django.urls import path
from profilepage.views import show_profile

app_name = 'profilepage'

urlpatterns = [
    path('', show_profile, name='show_profile'),
]