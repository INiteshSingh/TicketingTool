from django.shortcuts import render,get_object_or_404,redirect
from Ticket_Creation.models import Ticket
from . import forms
#View for a list dispaly for the raised tickets
def Ticket_Display(request):
    tickets = Ticket.objects.exclude(Ticket_Status = "CLOSED")
    return render(request,'Ticket_Analysis/List_View.html',{"tickets":tickets})

#view to update ticket, add notes, update the ticket status and resolution notes to a ticket
def Tickets_Working(request):
    tickets = Ticket.objects.exclude()
    return render(request,'Ticket_Analysis/List_View.html',{"tickets":tickets})

# this is where users should be able to work on the ticket and close/add notes to the ticket
"""
Requirements of this Function
1.Change the Status of the Ticket from NEW to CLOSED,IN_PROGRESS,RESOLVED etc depending on the situation
    For the Change to be made of the status Using a form as it allows for Adding the Data to the 
    notes

2.Add Notes that would be displayed when the ticket is searched

3.Show only the tickets that are active in the Ticket Analysis Page, since that would be the only point where the analyst 
would see the ticket
"""
def Detailed_View(request,ticket_number):

    ticket = get_object_or_404(
        Ticket,
        Ticket_Number=ticket_number
    )

    if request.method == "POST":

        form = forms.UpdateForm(request.POST,instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("detailed_view",ticket_number=ticket_number)
    else:
        form = forms.UpdateForm(instance=ticket)
    return render(request,'Ticket_Analysis/Detail_View.html',{"ticket":ticket,"form":form})     