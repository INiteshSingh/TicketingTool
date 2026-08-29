from django.urls import path
from . import views

urlpatterns = [
    path('User_Login/',views.login_page,name="user_login"),
    path('Admin/',views.Admin,name="Admin")
]