from add_review.views import *
from django.urls import path 

app_name = 'add_review'

urlpatterns= [
path("", get_books, name="get_books"),
path('add_review/<int:book_id>/', add_review, name='add_review'),

]