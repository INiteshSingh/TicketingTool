from django.urls import path

from . import views

urlpatterns = [
    path("RaiseTicket", views.ticket_form, name="ticket_form"),
]