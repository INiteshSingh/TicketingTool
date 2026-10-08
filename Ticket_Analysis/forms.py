from django import forms
from Ticket_Creation.models import Ticket
from Ticket_Analysis.models import Working_Notes

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["Ticket_Status","Working_Notes"]
        