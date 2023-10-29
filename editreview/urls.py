
from django.urls import path

from editreview.views import editreview, get_books, get_review,display_reviews
# from .views import show_main
# from main.views import show_main, create_product
# from main.views import show_main, create_product, show_xml 
# from main.views import show_main, create_product, show_xml, show_json
# from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, get_product_json, add_product_ajax
# from main.views import register #sesuaikan dengan nama fungsi yang dibuat
# from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
# from main.views import logout_user
# from main.views import edit_product
# from main.views import delete_product


app_name = 'editreview'

urlpatterns = [
    # path('', show_main, name='show_main'),
    # path('xml/', show_xml, name='show_xml'), 
    # path('json/', show_json, name='show_json'),
    # path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    # path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    # path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    # path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    # path('logout/', logout_user, name='logout'),
    path('<int:id>/', editreview, name='editreview'),
    # path('delete/<int:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
    # path('get-product/', get_product_json, name='get_product_json'),
    # path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
    path('get-review/<int:review_id>', get_review, name="get_review"),
    path('reviews/', display_reviews, name='display_reviews'),
    path("", get_review, name="get_review"),


]