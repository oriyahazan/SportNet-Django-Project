from django.test import TestCase
from .forms import RegisterForm, EventForm, MissionForm, PostForm

from blog import forms

class FormsTestCase(TestCase):
    def test_register_form(self):
        # Test that the RegisterForm form is valid with correct data
        form_data = {'full_name': 'John Smith', 'id_number': '1234567890', 'identity_qu': 'Driver License',
                     'place': 'New York', 'email': 'john@example.com', 'password': 'password123', 'role': 'admin',
                     'age': 25}
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test that the RegisterForm form is invalid with incorrect data
        form_data = {'full_name': '', 'id_number': '1234567890', 'identity_qu': 'Driver License', 'place': 'New York',
                     'email': 'john@example.com', 'password': 'password123', 'role': 'admin', 'age': 25}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_event_form(self):
        # Test that the EventForm form is valid with correct data
        form_data = {'title': 'Event 1', 'content': 'This is an event', 'date_posted': '2022-01-01',
                     'credit': 'John Smith', 'participants': 10}
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test that the EventForm form is invalid with incorrect data
        form_data = {'title': '', 'content': 'This is an event', 'date_posted': '2022-01-01', 'credit': 'John Smith',
                     'participants': 10}
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_mission_form(self):
        # Test that the MissionForm form is valid with correct data
        form_data = {'title': 'Mission 1', 'content': 'This is a mission'}
        form = MissionForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test that the MissionForm form is invalid with incorrect data
        form_data = {'title': '', 'content': 'This is a mission'}
        form = MissionForm(data=form_data)
        self.assertFalse(form.is_valid())