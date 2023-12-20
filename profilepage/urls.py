from django.urls import path
from profilepage.views import *

app_name = 'profilepage'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('create/', create_profile, name='create_profile'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('edit/', edit_profile_ajax, name='edit_profile'),
    path('get-profile/', get_profile_json, name='get_profile_json'),
    path('edit-flutter/', edit_profile_flutter, name= 'edit_profile_flutter'),
    path('create-flutter/<str:user_name>/', create_profile_flutter, name= 'create_profile_flutter'),
]
