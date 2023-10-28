from django.urls import path
from .views import *

app_name = "landing_page"

urlpatterns = [
    path("", get_books, name="get_books"),
    path("page/", show_landing_page, name="show_landing_page"),
    path("get_data_json/", get_data_json, name="get_data_json"),
    path("check_if_user_logged_in/", check_if_user_logged_in, name="check_if_user_logged_in"),
    path("get_faq_data/", get_faq_data, name="get_faq_data"),
    path("faq/data/", show_faq_data_json, name="show_faq_data_json"),
    path("faq/data/user/", get_faq_data_per_user, name="get_faq_data_per_user"),
    path("faq/question/", add_faq_question, name="add_faq_question")
]