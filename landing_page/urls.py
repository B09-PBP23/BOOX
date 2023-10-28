from django.urls import path
from .views import *

app_name = "landing_page"

urlpatterns = [
    path("", get_books, name="get_books"),
    path("page/", show_landing_page, name="show_landing_page"),
    path("get_data_json/", get_data_json, name="get_data_json"),
    path("book/review/data/<int:book_id>/", get_review_data, name="get_review_data"),
    path("book/review/<int:book_id>/", show_review, name="show_review"),
]