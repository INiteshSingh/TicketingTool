from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('Create_User/',views.create_user),
    path('User_Login/',LoginView.as_view(template_name="User_Management/login.html"),name="User_Login"),
    path('Admin/',views.Admin,name="Admin")
]