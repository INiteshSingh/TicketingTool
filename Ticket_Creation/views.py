from django.shortcuts import render, redirect
from tools import Tic_Gen
from .forms import TicketForm
from .models import Ticket
#To Print the Form data and then print the data into the terminal
def ticket_form(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
           ticket_obj = form.save(commit=False)
           ticket_obj.Ticket_Number = Tic_Gen(form.cleaned_data['Issue_Category'])
           ticket_obj.save()
        return render(request,"Ticket_Creation/ticket_raised.html",{"ticket_number":ticket_obj.Ticket_Number})
    else:
        form = TicketForm()
    return render(request, "Ticket_Creation/ticket_form.html", {"form": form})
