from django.shortcuts import render, redirect
from tools import Tic_Gen
from .forms import TicketForm,chat_bot_form
from .models import Ticket
#To Print the Form data and then print the data into the1 terminal

def home_page(request):
    return render(request,"Ticket_Creation/homepage.html")

"""This is a chatbot that the user is talking and trying to fix their issues with the solutions 
it provides"""
def chat_with_user(request):
    form = chat_bot_form()
    while True:
        if request.method == "POST":
            form = chat_bot_form(request.POST)
            if form.is_valid():
                user_query = form.cleaned_data["user_query"]
                chat_response = (user_query)
                return render(request,'Ticket_Creation/chatbot.html',{'form':form,'chat_response':chat_response})
        return render(request,'Ticket_Creation/chatbot.html',{'form':form})

# def ticket_form(request):
#     if request.method == "POST":
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             pass
#         return render(request,"Ticket_Creation/ticket_raised.html",{"ticket_number":ticket_obj.Ticket_Number})
#     else:
#         form = TicketForm()
#     return render(request, "Ticket_Creation/ticket_form.html", {"form": form})
