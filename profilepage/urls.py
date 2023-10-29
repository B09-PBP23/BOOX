from django.urls import path
from profilepage.views import *

app_name = 'profilepage'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('create/', create_profile, name='create_profile'),
    path('json/', show_json, name='show_json'), 
    path('edit/', edit_profile_ajax, name='edit_profile'),
    path('get-profile/', get_profile_json, name='get_profile_json'),
]