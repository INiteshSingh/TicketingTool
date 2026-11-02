from django import forms
from Ticket_Analysis.models import Ticket
from .models import WorkingNote

class WorkNoteForm(forms.ModelForm):
    class Meta:
        model = WorkingNote
        fields = ["note","author"]