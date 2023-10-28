from django.urls import path
from landing_page.views import get_data_json

from readers_favorite.views import add_comment, add_upvote_ajax, get_user_info, show_readers_favorite

app_name = 'readers_favorite'

urlpatterns = [
    path('', show_readers_favorite, name='show_readers_favorite'),
    path("get_data_json/", get_data_json, name="get_data_json"),
    path('add_upvote_ajax/<int:item_id>/', add_upvote_ajax, name='add_upvote_ajax'),
    path('get_user_info/', get_user_info, name='get_user_info'),
    path('add_comment/', add_comment, name='add_comment'),


]