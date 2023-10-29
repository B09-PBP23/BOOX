from django.urls import path

from landing_page.views import get_data_json, show_landing_page
from bookmarks.views import add_to_bookmark, get_books, remove_from_bookmark, show_bookmarks, make_bookmarks

app_name = "bookmarks"

urlpatterns = [
    path("", get_books, name="get_books"),
    path("page/", show_landing_page, name="show_landing_page"),
    path("get_data_json/", get_data_json, name="get_data_json"),
    path("add_to_bookmark/<int:book_id>/", add_to_bookmark, name="add_to_bookmark"),
    path("remove_from_bookmark/<int:book_id>/", remove_from_bookmark, name="remove_from_bookmark"),
    path("show_bookmarks/", show_bookmarks, name="show_bookmarks"),
    path("make_bookmarks/", make_bookmarks, name = "make_bookmarks")
]
