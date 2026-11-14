from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect

from Ticket_Creation.models import Ticket
from Ticket_Creation.forms import TicketForm
from .forms import WorkNoteForm, ticketStatusUpdate


def all_tickets(request):
    # Show tickets in the selected statuses
    tickets = Ticket.objects.filter(
        Ticket_Status__in=["NEW", "CLOSED", "IN_PROGRESS", "ON_HOLD"]
    )

    return render(
        request,
        "Ticket_Analysis/List_View.html",
        {"tickets": tickets},
    )


def detail_view(request, ticket_number):

    # Retrieve the ticket using its ticket number (404 if it doesn't exist)
    ticket = get_object_or_404(Ticket, Ticket_Number=ticket_number)

    if request.method == "POST":
        # Both forms are submitted together with the single "Update" button.
        # Prefixes keep their field names from clashing in one POST.
        ticketUpdateForm = ticketStatusUpdate(
            request.POST, instance=ticket, prefix="status"
        )
        form = WorkNoteForm(request.POST, prefix="note")

        # Save only if BOTH are valid, so we never end up with half an update
        if ticketUpdateForm.is_valid() and form.is_valid():
            with transaction.atomic():
                ticketUpdateForm.save()

                # Save a note only if the user actually typed something
                if form.has_changed():
                    working_note = form.save(commit=False)
                    working_note.Ticket = ticket
                    working_note.save()

            # Post/Redirect/Get: stops a browser refresh from re-submitting
            return redirect(request.path)
    else:
        ticketUpdateForm = ticketStatusUpdate(instance=ticket, prefix="status")
        form = WorkNoteForm(prefix="note")

    # Fetched after any save so the list is always current
    notes = ticket.work_notes.all()

    return render(
        request,
        "Ticket_Analysis/Detailed_View.html",
        {
            "ticket": ticket,
            "form": form,
            "notes": notes,
            "ticketUpdateForm": ticketUpdateForm,
        },
    )


def dynamic_details(request, ticket_number):
    ticketDetails = get_object_or_404(Ticket, Ticket_Number=ticket_number)

    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticketDetails)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = TicketForm(instance=ticketDetails)

    return render(
        request,
        "Ticket_Analysis/DynamicDetails.html",
        {"ticketDetails": ticketDetails, "form": form},
    )