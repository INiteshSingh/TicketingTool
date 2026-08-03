from django.shortcuts import render
from Ticket_Creation.models import Ticket

#View for a list dispaly for the raised tickets
def Tickets_View(request):
    tickets = Ticket.objects.all()
    return render(request,'Ticket_Analysis/List_View.html',{"tickets":tickets})
