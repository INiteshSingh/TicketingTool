from django.db import models
from Ticket_Creation.models import Ticket

class workingNotes(models.Model):
    Ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    notes = models.TextField(null=False)
    author = models.TextField()

    def __str__(self):
       return self.notes