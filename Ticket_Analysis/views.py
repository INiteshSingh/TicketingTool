from django.shortcuts import render,get_object_or_404
from Ticket_Creation.models import Ticket
#View for a list dispaly for the raised tickets
def Ticket_Display(request):
    tickets = Ticket.objects.all()
    return render(request,'Ticket_Analysis/List_View.html',{"tickets":tickets})

#view to update ticket, add notes, update the ticket status and resolution notes to a ticket
def Tickets_Working(request):
    tickets = Ticket.objects.all()
    return render(request,'Ticket_Analysis/List_View.html',{"tickets":tickets})

# this is where users should be able to work on the ticket and close/add notes to the ticket

"""
Requirements of this Function
1.Change the Status of the Ticket from NEW to CLOSED,IN_PROGRESS,RESOLVED etc depending on the situation
2.Add Notes that would be displayed when the ticket is searched
"""
def Detailed_View(request,ticket_number):
    ticket = get_object_or_404(
        Ticket,
        Ticket_Number=ticket_number
    )
    return render(request,'Ticket_Analysis/Detail_View.html',{"ticket":ticket})     