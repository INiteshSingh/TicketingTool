from django.shortcuts import render, redirect
from tools import Tic_Gen
from .forms import TicketForm
from .models import Ticket
#To Print the Form data and then print the data into the terminal
def ticket_form(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            print(form.data)
            form.save()
            print("Data is Saved")

    form = TicketForm()
    return render(request, "Ticket_Creation/ticket_form.html", {"form": form})
