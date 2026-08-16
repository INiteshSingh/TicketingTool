from django.urls import path
from . import views
urlpatterns =[
    path("",views.Ticket_Display,name="List View"),
    path("ticket/<str:ticket_number>/",views.Detailed_View,name='detailed_view'),
]