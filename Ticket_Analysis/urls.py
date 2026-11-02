from django.urls import path
from . import views
urlpatterns = [
    path("list/",views.all_tickets,name="list"),
    path("ticket/<str:ticket_number>",views.detail_view,name="detailed_view")
]