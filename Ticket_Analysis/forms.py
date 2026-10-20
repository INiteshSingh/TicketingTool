from django import forms
from Ticket_Creation.models import Ticket
from Ticket_Analysis.models import workingNotes

class workingNotesForm(forms.ModelForm):
    class Meta:
        model = workingNotes
        fields = ['notes','author']
        