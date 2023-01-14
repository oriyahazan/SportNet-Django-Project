# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from .models import Post, DocEvent
# from blog import views
#
# class CommunityViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = get_user_model().objects.create_user(
#             full_name='Test User',
#             email='testuser@example.com',
#             password='testpassword',
#             credit=100
#         )
#         self.post = Post.objects.create(
#             title='Test Post',
#             content='This is a test post.',
#             author=self.user,
#             credit=50,
#             flag='1'
#         )
#         self.url = reverse('blog-community')
#
#     def test_community_view_redirects_if_not_logged_in(self):
#         response = self.client.get(self.url)
#         self.assertRedirects(response, '/accounts/login/?next=' + self.url)
#
#     def test_community_view_uses_correct_template(self):
#         self.client.login(email='testuser@example.com', password='testpassword')
#         response = self.client.get(self.url)
#         self.assertTemplateUsed(response, 'blog/HomePageCommunity.html')
#
#     def test_community_view_displays_all_posts(self):
#         self.client.login(email='testuser@example.com', password='testpassword')
#         response = self.client.get(self.url)
#         self.assertContains(response, self.post.title)
#
#     def test_community_view_reduces_user_credit_on_post_purchase(self):
#         self.client.login(email='testuser@example.com', password='testpassword')
#         self.client.post(self.url, {'csrfmiddlewaretoken': 'randomstring', '1': '1'})
#         self.user.refresh_from_db()
#         self.assertEqual(self.user.credit, 50)
#
#     def test_community_view_creates_DocEvent_on_post_purchase(self):
#         self.client.login(email='testuser@example.com', password='testpassword')
#         self.client.post(self.url, {'csrfmiddlewaretoken': 'randomstring', '1': '1'})
#         doc_event = DocEvent.objects.get(title='Test Post')
#         self.assertEqual(doc_event.content, 'This is a test post.')
#         self.assertEqual(doc_event.parti, self.user)
#         self.assertEqual(doc_event.credit, 50)
