from django import forms
from Ticket_Creation.models import Ticket
from Ticket_Analysis.models import Working_Notes

class Working_Notes(forms.ModelForm):
    class Meta:
        model = Working_Notes
        fields = ['Working_Notes']
        