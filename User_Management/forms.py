from django import forms
from .models import  User

class User_Creation_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Employee_ID','name','password']

    def save(self,commit=True):
        Employee_ID = self.cleaned_data['Employee_ID']
        password = self.cleaned_data['password']
        name = self.cleaned_data['name']

        user = user.objects.create_user(
            Employee_ID=Employee_ID,
            password=password,
            name=name
        )

        return User