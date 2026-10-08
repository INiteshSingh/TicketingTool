from django.db import models
from Ticket_Creation.models import Ticket
from django.conf import settings

# Create your models here.
class Working_Notes(models.Model):
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,
    related_name="working_notes")
    def __str__(self):
        return self.related_notes

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
    null=True)

     = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticke.Ticket_Number} = {self.author}"
