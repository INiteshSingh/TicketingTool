from django.shortcuts import render, redirect
# from tools import Tic_Gen
from .forms import TicketForm,chat_bot_form
from .models import Ticket
from django.contrib.auth.decorators import login_required
from tools import chat_with_ai
#To Print the Form data and then print the data into the1 terminal

@login_required
def home_page(request):
    return render(request,"Ticket_Creation/home.html")

@login_required
def chat_bot_interface(request):
    if request.method == "POST":
        pass #some code that sends the user query to the model and some that sends back the response to and fro
        form = chat_bot_form(request.POST)
        if form.is_valid():
           response = chat_with_ai(form.changed_data["user_query"])
           return render(request,"Ticket_Creation/chatbot.html",{"response":response})
    return render(request,"Ticket_Creation/chatbot.html")

@login_required
def ticket_form(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
            ticket_number = f"INC{ticket.id:06d}"
            ticket.Ticket_Number = ticket_number
            ticket.save()
            return redirect("Ticket Raised",ticket_number)
        else:
            err_msg = "Invalid details, check your details and try again"
            return render(request,"Ticket_Creation/ticket_form.html",{"err_msg":err_msg})
    form = TicketForm()
    return render(request,'Ticket_Creation/ticket_form.html',{'form':form})

@login_required
def ticket_raised(request,ticket_number):
    return render(request,"Ticket_Creation/ticket_raised.html",{"ticket_number":ticket_number})

def ticket_status(request):
    return render(request,"Ticket_Creation/ticket_status.html")

def get_help(request):
    return render(request,"Ticket_Creation/chatbot.html")