from django.shortcuts import render, redirect,get_object_or_404
# from tools import Tic_Gen
import json
from .forms import TicketForm,ticket_status_form
from .models import Ticket
from django.contrib.auth.decorators import login_required
from tools import chat_with_ai
from django.http import JsonResponse
from django.urls import reverse
#To Print the Form data and then print the data into the1 terminal

@login_required
def home_page(request):
    return render(request,"Ticket_Creation/home.html")

@login_required
def chat_bot_interface(request):
    if request.method == "POST":
        body = json.loads(request.body)
        prompt = body.get('prompt')
        ai_result = chat_with_ai(prompt)
        response = ai_result["response"]
        print(prompt)
        print(response)
        print(ai_result['Raise_Ticket'])
        if ai_result['Raise_Ticket'] == True:
            return JsonResponse({
                "redirect":True,
                "url":reverse("Raise A Ticket")
            })
        return JsonResponse({
            "redirect":False,
            "response":response})
    return render(request,'Ticket_Creation/chatbot.html')

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
    if request.method == 'POST':
        form = ticket_status_form(request.POST)
        if form.is_valid():
            ticket_number = form.cleaned_data['Ticket_Number']
            try:
                ticket = Ticket.objects.get(Ticket_Number=ticket_number)
                return render(request,'Ticket_Creation/ticket_status.html',{'ticket': ticket})
            except Ticket.DoesNotExist:
                return render(request,'Ticket_Creation/ticket_status.html',{'error_message': 'Ticket not found.'})
    else:
        form = ticket_status_form()
    return render(request, 'Ticket_Creation/ticket_status.html', {'form': form})

