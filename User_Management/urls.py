from django.urls import path
from . import views

urlpatterns = [
    path('Create_User/',views.create_user),
    path('User_Login/',views.login_page,name="User_Login"),
    path('Admin/',views.Admin,name="Admin")
]