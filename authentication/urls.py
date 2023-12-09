from django.urls import path
from .views import register, login_user, logout_user, flutter_login, flutter_register, flutter_logout

app_name = 'authentication'

urlpatterns = [
  path('register/', register, name='register'),
  path('login/', login_user, name='login'), 
  path('logout/', logout_user, name='logout'),
  path('flutter_login/', flutter_login, name='flutter_login'),
  path('flutter_register/', flutter_register, name='flutter_register'),
  path('flutter_logout/', flutter_logout, name='flutter_logout'),
]