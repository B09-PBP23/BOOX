from django.urls import path
from landing_page.views import get_data_json

from readers_favorite.views import add_upvote_ajax, show_readers_favorite

app_name = 'readers_favorite'

urlpatterns = [
    path('readers_favorite/', show_readers_favorite, name='readers-favorite'),
    # path('readers_favorite/get_book_info/', get_book_info, name='get_book_info'),
    path("readers_favorite/get_data_json/", get_data_json, name="get_data_json"),
    path('readers_favorite/add_upvote_ajax/<int:item_id>/', add_upvote_ajax, name='add_upvote_ajax'),
    # path('readers_favorite/get_books/',get_books, name='get_books'), 
]