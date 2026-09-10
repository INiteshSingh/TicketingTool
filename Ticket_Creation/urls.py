from django.urls import path

from . import views

urlpatterns = [
    path("Home", views.home_page, name="Home"),
    path("Raise Ticket",views.ticket_form,name='Raise A Ticket'),
    path("Track Ticket",views.ticket_status,name="Track Ticket"),
    path("Get Support",views.get_help,name="Get Support")
]