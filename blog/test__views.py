from django.test import TestCase, Client
from .models import User, Event, Mission, Post

#from blog import models -- 1st try
#from .forms import RegisterForm, EventForm, MissionForm, PostForm -- don't work


class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a client to send HTTP requests
        self.client = Client()

        # Create a user
        User.objects.create(full_name='John Smith', id_number='1234567890', identity_qu='Driver License',
                            place='New York', role='admin', email='john@example.com', password='password123', age=25)

        # Create an event
        Event.objects.create(title='Event 1', content='This is an event', credit=0, participants=10)

        # Create a mission
        Mission.objects.create(title='Mission 1', content='This is a mission')

        # Create a post
        Post.objects.create(title='Post 1', content='This is a post', credit=0,
                            author=User.objects.get(full_name='John Smith'))

    def test_home_view(self):
        # Send a GET request to the home view
        response = self.client.get('/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the correct number of posts
        self.assertEqual(len(response.context['posts']), 1)

    def test_posts_view(self):
        # Send a GET request to the posts view
        response = self.client.get('/posts/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the correct number of posts
        self.assertEqual(len(response.context['posts']), 1)

    def test_about_view(self):
        # Send a GET request to the about view
        response = self.client.get('/about/')

a