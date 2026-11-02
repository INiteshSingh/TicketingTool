from django.shortcuts import render, get_object_or_404
from Ticket_Creation.models import Ticket
from .forms import WorkNoteForm


def all_tickets(request):
    # Show tickets in the selected statuses
    tickets = Ticket.objects.filter(
        Ticket_Status__in=["NEW", "CLOSED", "IN_PROGRESS", "ON_HOLD"]
    )

    return render(
        request,
        'Ticket_Analysis/List_View.html',
        {'tickets': tickets}
    )


def detail_view(request, ticket_number):

    # Retrieve the ticket using its ticket number
    ticket_details = get_object_or_404(
        Ticket,
        Ticket_Number=ticket_number
    )

    # Retrieve all working notes associated with this ticket
    notes = ticket_details.work_notes.all()

    if request.method == "POST":
        form = WorkNoteForm(request.POST)

        if form.is_valid():

            # Create an unsaved working-note object
            working_note = form.save(commit=False)

            # Associate the note with the current ticket
            working_note.Ticket = ticket_details

            # Save the working note
            working_note.save()

            # Refresh the notes displayed on the page
            notes = ticket_details.work_notes.all()

            # Show a fresh form after successful submission
            form = WorkNoteForm()

    else:
        form = WorkNoteForm()
    
    return render(
        request,
        'Ticket_Analysis/Detailed_View.html',
        {
            'ticket': ticket_details,
            'form': form,
            'notes': notes
        }
    )