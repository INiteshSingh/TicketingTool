from django import forms
from Ticket_Creation.models import Ticket

<<<<<<< Updated upstream
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "Issue_Category","Short_Description","Complete_Description","User_Contact","Raised_By"
        ]        

class chat_bot_form(forms.Form):
    user_query = forms.CharField(max_length=300)
=======
class TicketForm(forms.Form):
    question = forms.CharField(max_length=225)
        
>>>>>>> Stashed changes
