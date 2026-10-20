from django.shortcuts import render,get_object_or_404,redirect
from Ticket_Creation.models import Ticket
from Ticket_Analysis.models import workingNotes
from .forms import workingNotesForm
from django.contrib.auth.decorators import login_required
#View for a list dispaly for the raised tickets


def Ticket_Display(request):
    tickets = Ticket.objects.filter(
        Ticket_Status__in=["NEW","In Progress","On Hold"]
    )
    # tickets = Ticket.objects.all()
    return render(request,'Ticket_Analysis/List_View.html',{"tickets":tickets})

#view to update ticket, add notes, update the ticket status and resolution notes to a ticket
def Tickets_Working(request):
    tickets = Ticket.objects.exclude()
    return render(request,'Ticket_Analysis/List_View.html',{"tickets":tickets})

# this is where users should be able to work on the ticket and close/add notes to the ticket

@login_required
def Detailed_View(reqeust,ticket_number):
    ticketDetails = Ticket.objects.get(Ticket,Ticket_Number = ticket_number)
    working_Notes = Ticket.notes.all()
    form = workingNotesForm()
    if request.method == "POST":
        form = workingNotesForm(request.POST)
        if form.is_valid():
            print(f"{form.cleaned_data['notes']} added by {form.cleaned_data['author']}")
            form.save()
        return render(reqeust,"Ticket_Analysis/Detail_View.html",{'form':form,'ticket':ticketDetails,'workingNotes':working_Notes})
    return render(request,'Ticket_Analysis/Detail_View',{'form:':form,'ticket':ticketDetails,'workingNotes':working_Notes})