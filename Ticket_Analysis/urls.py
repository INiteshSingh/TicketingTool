from django.urls import path
from . import views
urlpatterns =[
    path("list",views.Ticket_Display),
    path("ticket/<str:ticket_number>/",views.Detailed_View,name="detailed_view"),
    path("working",views.Tickets_Working)
]