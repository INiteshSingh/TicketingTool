from django.shortcuts import render
from . import forms
# Create your views here.

def create_user(request):
    form = forms.User_Creation_form()
    if request.method =="POST":
        form = forms.User_Creation_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('User_Login')
    return render(request,'User_Management/create_user.html',{'form':form}
    )


def login_page(request):
    return render(request,'User_Management/login.html')


def Admin(request):
    pass

