from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import login,logout,authenticate
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
    form = forms.login_form()
    if request.method == "POST":
        form = forms.login_form(request.POST)
        if form.is_valid():
            Employee_Id = form.cleaned_data['Employee_ID']
            password = form.cleaned_data['password']
            user = authenticate(Employee_Id,password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_msg = "Username or Password is Invalid"
                return render(request,'')
    return render(request,'User_Management/login.html')


def Admin(request):
    pass

