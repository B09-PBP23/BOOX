from django.urls import path
from landing_page.views import get_data_json

from readers_favorite.views import add_comment, add_upvote_ajax, get_all_comments, get_commenters, get_username_by_id, show_readers_favorite

app_name = 'readers_favorite'

urlpatterns = [
    path('', show_readers_favorite, name='show_readers_favorite'),
    path("get_data_json/", get_data_json, name="get_data_json"),
    path('add_upvote_ajax/<int:item_id>/', add_upvote_ajax, name='add_upvote_ajax'),
    path('get_username_by_id/<int:user_id>/', get_username_by_id, name='get_username_by_id'),
    path('get_all_comments/', get_all_comments, name='get_all_comments'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('get_commenters/', get_commenters, name='get_commenters'),
    path('add_comment/', add_comment, name='add_comment'),
]
=======
    path('get_commeSnters/', get_commenters, name='get_commenters'),
    path('add_comment/', add_comment, name='add_comment'),
]
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
=======
    path('get_commeSnters/', get_commenters, name='get_commenters'),
    path('add_comment/', add_comment, name='add_comment'),
]
>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
