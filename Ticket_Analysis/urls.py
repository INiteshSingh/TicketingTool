from django.urls import path
from . import views
urlpatterns =[
    path("",views.Tickets_View,name='List_View')
]