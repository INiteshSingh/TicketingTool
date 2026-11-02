from django.db import models
from Ticket_Creation.models import Ticket
# Create your models here.
class WorkingNote(models.Model):
    Ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name="work_notes")
    note = models.TextField()
    author = models.CharField(max_length=32)
    timeAddedAt = models.DateTimeField(auto_now_add=True)
    
