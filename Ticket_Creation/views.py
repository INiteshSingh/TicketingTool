from django.shortcuts import render, redirect
from tools import Tic_Gen
from .forms import TicketForm,chat_bot_form
from .models import Ticket
#To Print the Form data and then print the data into the1 terminal

def home_page(request):
    return render(request,"Ticket_Creation/homepage.html")

def ticket_form(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            print("In Views",form.cleaned_data)
            issue_category = form.cleaned_data['Issue_Category']
            Tic_Gen(issue_category,**form.cleaned_data)
            Ticket = form.save()
            return render(request,"Ticket_Creation/ticket_raised.html",{"ticket_number":Ticket})
        elif form:
            pass
    else:
        form = TicketForm()
    return render(request, "Ticket_Creation/chatbot.html", {"form": form})

