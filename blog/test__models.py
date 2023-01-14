from django.test import TestCase
from blog import models

class ModelsTestCase(TestCase):
    def setUpClass(self):
        # Create a user
        User.objects.create(full_name='John Smith', id_number='1234567890', identity_qu='Driver License',
                            place='israel', role='admin', email='john@example.com', password='password123', age=25)

        # Create an event
        Event.objects.create(title='Event 1', content='This is an event', credit=0, participants=10)

        # Create a mission
        Mission.objects.create(title='Mission 1', content='This is a mission')

        # Create a post
        Post.objects.create(title='Post 1', content='This is a post', credit=0,
                            author=User.objects.get(full_name='John Smith'))

    def test_user_model(self):
        # Test the user model
        user = User.objects.get(full_name='John Smith')
        self.assertEqual(user.id_number, '1234567890')
        self.assertEqual(user.identity_qu, 'Driver License')
        self.assertEqual(user.place, 'israel')
        self.assertEqual(user.role, 'admin')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.age, 25)

    def test_event_model(self):
        # Test the event model
        event = Event.objects.get(title='Event 1')
        self.assertEqual(event.content, 'This is an event')
        self.assertEqual(event.credit, 0)
        self.assertEqual(event.participants, 10)

    def test_mission_model(self):
        # Test the mission model
        mission = Mission.objects.get(title='Mission 1')
        self.assertEqual(mission.content, 'This is a mission')

    def test_post_model(self):
        # Test the post model
        post = Post.objects.get(title='Post 1')
        self.assertEqual(post.content, 'This is a post')
        self.assertEqual(post.credit, 0)
        self.assertEqual(post.author.full_name, 'John Smith')
