from django.urls import path

from . import views

urlpatterns = [
    path("home_page", views.home_page, name="home_page"),
    path("chat",views.chat_with_user, name="chat")
]