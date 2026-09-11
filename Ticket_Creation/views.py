from django.shortcuts import render, redirect
from tools import Tic_Gen
from .forms import TicketForm,chat_bot_form
from .models import Ticket
#To Print the Form data and then print the data into the1 terminal

def home_page(request):
    return render(request,"Ticket_Creation/home.html")

def ticket_form(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            issue_category = form.cleaned_data["Issue_Category"]
            Ticket = Tic_Gen(issue_category)
            ticket.Ticket_Number = Ticket
            ticket.save()
            return redirect("Ticket Raised",Ticket)
        else:
            err_msg = "Invalid details, check your details and try again"
            return render(request,"Ticket_Creation/ticket_form.html",{"err_msg":err_msg})
    form = TicketForm()
    return render(request,'Ticket_Creation/ticket_form.html',{'form':form})


def ticket_raised(request,ticket_number):
    return render(request,"Ticket_Creation/ticket_raised.html",{"ticket_number":ticket_number})

def ticket_status(request):
    return render(request,"Ticket_Creation/ticket_status.html")

def get_help(request):
    return render(request,"Ticket_Creation/chatbot.html")