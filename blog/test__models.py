from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from.models import user, Event, Mission, Post, Image, Rating, CreateGuide, Donate, DocEvent

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = get_user_model()
        user = user.objects.create(
            full_name='Test User',
            email='testuser@example.com',
            id_number=1234567890,
            identity_qu='Passport',
            place='US',
            role='Admin',
            age=30,
            flag='1',
            credit=100,
            password='testpassword'
        )
        self.assertEqual(user.full_name, 'Test User')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.id_number, 1234567890)
        self.assertEqual(user.identity_qu, 'Passport')
        self.assertEqual(user.place, 'US')
        self.assertEqual(user.role, 'Admin')
        self.assertEqual(user.age, 30)
        self.assertEqual(user.flag, '1')
        self.assertEqual(user.credit, 100)

    def test_user_email_validation(self): ''' this test show that we dont get attention if the user dont write @ in his email'''
        user = get_user_model()
        with self.assertRaises(ValidationError):
            user = user.objects.create(
                full_name='Test User',
                email='invalid.email',
                password='testpassword'
            )


    def test_event_creation(self):
        event = Event.objects.create(
            title='Test Event',
            content='This is a test event.',
            credit=100,
            participants=5
        )
        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(event.content, 'This is a test event.')
        self.assertEqual(event.credit, 100)
        self.assertEqual(event.participants, 5)

    def test_mission_creation(self):
        mission = Mission.objects.create(
            title='Test Mission',
            content='This is a test mission.'
        )
        self.assertEqual(mission.title, 'Test Mission')
        self.assertEqual(mission.content, 'This is a test mission.')
