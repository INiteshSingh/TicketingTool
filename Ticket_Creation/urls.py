from django.urls import path

from . import views

urlpatterns = [
    path("home_page", views.home_page, name="home_page"),
    path("ticket_form",views.ticket_form, name="Raise A Ticket")
]