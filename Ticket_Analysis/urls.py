from django.urls import path
from . import views
urlpatterns =[
    path("list",views.Ticket_Display,name="List View"),
    path("detailed_view/<str:ticket_number>/",views.Detailed_View,name='detailed_view'),
]