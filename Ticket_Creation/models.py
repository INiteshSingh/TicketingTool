from django.db import models

# Create your models here.
class Ticket(models.Model):
    Issue_Type = [
        ("Access Issue", "Access Issue"),
        ("Item Request", "Item Request"),
        ("Hardware Issue", "Hardware Issue"),
        ("General Issue", "General Issue"),
    ]
    #the one on the First gets stored and the one on the left is displayed on the form in the page
    Status=[
        ("NEW","New"),
        ("CLOSED","Closed"),
        ("IN_PROGRESS","In Progress"),
        ("ON_HOLD","On Hold"),      
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
