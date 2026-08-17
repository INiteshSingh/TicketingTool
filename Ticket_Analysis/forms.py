from django import forms
from Ticket_Creation.models import Ticket

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["Ticket_Status","Working_Notes"]
        