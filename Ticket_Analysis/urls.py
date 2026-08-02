from django.urls import path
from . import views
url_patterns =[
    path('List_View',views.Tickets_View,name='List_View')
]