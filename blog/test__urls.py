from django.test import TestCase
from django.urls import reverse, resolve

from blog import views
#from . import views

class UrlsTestCase(TestCase):

    # def test_home_url(self):
    #     url = reverse('')
    #     self.assertEqual(url, '/')
    #     resolver_match = resolve('/')
    #     self.assertEqual(resolver_match.func, views.home)



    # def test_posts_url(self):
    #     url = reverse('blog-CreatPost')
    #     self.assertEqual(url, '/CreatPost/')
    #     resolver_match = resolve('/CreatPost/')
    #     self.assertEqual(resolver_match.func, views.CreatPost)

    # takin
    # def test_register_url(self):
    #     url = reverse('blog-register')
    #     self.assertEqual(url, '/register/')
    #     resolver_match = resolve('/register/')
    #     self.assertEqual(resolver_match.func, views.register)

    #takin
    # def test_homePage_url(self):
    #     url = reverse('blog-HomePage')
    #     self.assertEqual(url, '/HomePage/')
    #     resolver_match = resolve('/HomePage/')
    #     self.assertEqual(resolver_match.func, views.home)

    # def test_login_url(self):
    #     url = reverse('blog-login')
    #     self.assertEqual(url, '/login/')
    #     resolver_match = resolve('/login/')
    #     self.assertEqual(resolver_match.func, views.login)
