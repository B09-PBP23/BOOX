from add_review.views import *
from django.urls import path 

app_name = 'add_review'

urlpatterns= [
    path('add_review_ajax/', add_review_ajax, name='add_review_ajax'),
    path('show_review/<int:book_id>/', show_review, name='show_review'),
    path('get_reviews/<int:book_id>', get_reviews, name='get_reviews'),
    path('get_review_by_user/<int:book_id>', get_review_by_user, name='get_review_by_user'),
    path('get_username/<int:book_id>', get_username, name='get_username'),
]