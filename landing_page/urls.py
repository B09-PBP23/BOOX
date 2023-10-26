from django.urls import path
from .views import *

app_name = "landing_page"

urlpatterns = [
    path("", get_books, name="get_books"),
    path("page/", show_landing_page, name="show_landing_page"),
    path("get_data_json/", get_data_json, name="get_data_json")
]