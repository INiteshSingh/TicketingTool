from django.db import models

# Create your models here.
class Ticket(models.Model):
    Issue_Type = [
        ("access", "Access Issue"),
        ("request", "Item Request"),
        ("hardware", "Hardware Issue"),
        ("general", "General Issue"),
    ]
    #the one on the First gets stored
    Status=[
        ("NEW","New"),
        ("CLOSED","Closed"),
        ("IN_PROGRESS","In Progress"),
        ("RESOLVED","Resolved")
    ]
    Ticket_Number = models.CharField(max_length=12,null=False,unique=True)
    Raised_By = models.CharField(max_length=30,null=False)
    Raised_At = models.DateField(auto_now=True) #
    Short_Description = models.TextField(max_length=30)
    Complete_Description = models.TextField(max_length=100)
    Ticket_Status = models.CharField(max_length=20,choices=Status,default="NEW")
    User_Contact = models.CharField(max_length=12)
    Issue_Category = models.CharField(max_length=20,choices=Issue_Type)
    Working_Notes = models.TextField()
    Resolution_Notes = models.TextField()
