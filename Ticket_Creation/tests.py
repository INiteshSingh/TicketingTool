from django.test import TestCase
from django.urls import reverse

from .forms import TicketForm


class TicketFormTests(TestCase):
    def test_form_contains_expected_fields(self):
        form = TicketForm()
        self.assertIn("issue_type", form.fields)
        self.assertIn("short_description", form.fields)
        self.assertIn("long_description", form.fields)
        self.assertIn("contact_details", form.fields)
        self.assertIn("work_timings", form.fields)

    def test_ticket_form_page_loads(self):
        response = self.client.get(reverse("ticket_form"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Issue Type")
