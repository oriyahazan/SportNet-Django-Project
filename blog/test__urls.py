from django.test import TestCase
from django.urls import reverse, resolve

from blog import views
#from . import views

class UrlsTestCase(TestCase):

    def test_register_url(self):
        url = reverse('blog-register')
        self.assertEqual(url, '/register/')
        resolver_match = resolve('/register/')
        self.assertEqual(resolver_match.func, views.register)

    def test_homePageCommunity_url(self):
        url = reverse('blog-community')
        self.assertEqual(url, '/HomePageCommunity/')
        resolver_match = resolve('/HomePageCommunity/')
        self.assertEqual(resolver_match.func, views.home)

    def test_homePageAdmin_url(self):
        url = reverse('blog-admin')
        self.assertEqual(url, '/HomePageAdmin/')
        resolver_match = resolve('/HomePageAdmin/')
        self.assertEqual(resolver_match.func, views.home)

    def test_login_url(self):
        url = reverse('blog-login')
        self.assertEqual(url, '/login/')
        resolver_match = resolve('/login/')
        self.assertEqual(resolver_match.func, views.login)

    def test_home_url(self):
        url = reverse('blog.urls')
        self.assertEqual(url, '/')
        resolver_match = resolve('/')
        self.assertEqual(resolver_match.func, views.home)

    def test_homePageOrganization_url(self):
        url = reverse('blog-organization')
        self.assertEqual(url, '/HomePageOrganization/')
        resolver_match = resolve('/HomePageOrganization/')
        self.assertEqual(resolver_match.func, views.organization)

    def test_creatEvent_url(self):
        url = reverse('blog-CreatEvent')
        self.assertEqual(url, '/CreatEvent/')
        resolver_match = resolve('/CreatEvent/')
        self.assertEqual(resolver_match.func, views.CreatEvent)

    def test_creatMission_url(self):
        url = reverse('blog-CreatMission')
        self.assertEqual(url, '/CreatMission/')
        resolver_match = resolve('/CreatMission/')
        self.assertEqual(resolver_match.func, views.CreatMission)

    def test_allDocOrg_url(self):
        url = reverse('blog-AllDocOrg')
        self.assertEqual(url, '/AllDocOrg/')
        resolver_match = resolve('/AllDocOrg/')
        self.assertEqual(resolver_match.func, views.AllDocOrg)

    def test_missionPage_url(self):
        url = reverse('blog-missions')
        self.assertEqual(url, '/MissionPage/')
        resolver_match = resolve('/MissionPage/')
        self.assertEqual(resolver_match.func, views.missions)

    def test_allDocAdm_url(self):
        url = reverse('blog-AllDocAdm')
        self.assertEqual(url, '/AllDocAdm/')
        resolver_match = resolve('/AllDocAdm/')
        self.assertEqual(resolver_match.func, views.AllDocAdm)

    def test_comUserPage_url(self):
        url = reverse('blog-ComUserPage')
        self.assertEqual(url, '/ComUserPage/')
        resolver_match = resolve('/ComUserPage/')
        self.assertEqual(resolver_match.func, views.ComUserPage)

    def test_creatPost_url(self):
        url = reverse('blog-CreatPost')
        self.assertEqual(url, '/CreatPost/')
        resolver_match = resolve('/CreatPost/')
        self.assertEqual(resolver_match.func, views.CreatPost)

    def test_orgUserPage_url(self):
        url = reverse('blog-OrgUserPage')
        self.assertEqual(url, '/OrgUserPage/')
        resolver_match = resolve('/OrgUserPage/')
        self.assertEqual(resolver_match.func, views.OrgUserPage)

    def test_deleteUser_url(self):
        url = reverse('blog-deleteUsers')
        self.assertEqual(url, '/DeleteUsers/')
        resolver_match = resolve('/DeleteUsers/')
        self.assertEqual(resolver_match.func, views.deleteUsers)

    def test_userAuth_url(self):
        url = reverse('blog-UserAuth')
        self.assertEqual(url, '/UserAuth/')
        resolver_match = resolve('/UserAuth/')
        self.assertEqual(resolver_match.func, views.UserAuth)

    def test_postAuth_url(self):
        url = reverse('blog-PostAuth')
        self.assertEqual(url, '/PostAuthorization/')
        resolver_match = resolve('/PostAuthorization/')
        self.assertEqual(resolver_match.func, views.PostAuth)

    def test_trainingRating_url(self):
        url = reverse('blog-TrainingRating')
        self.assertEqual(url, '/TrainingRating/')
        resolver_match = resolve('/TrainingRating/')
        self.assertEqual(resolver_match.func, views.CreateRating)

    def test_activityReport_url(self):
        url = reverse('blog-ActivityReport')
        self.assertEqual(url, '/ActivityReport/')
        resolver_match = resolve('/ActivityReport/')
        self.assertEqual(resolver_match.func, views.ActivityReport)

    def test_allDocCom_url(self):
        url = reverse('blog-AllDocCom')
        self.assertEqual(url, '/AllDocCom/')
        resolver_match = resolve('/AllDocCom/')
        self.assertEqual(resolver_match.func, views.AllDocCom)

    def test_traningDoc_url(self):
        url = reverse('blog-TraningDoc')
        self.assertEqual(url, '/TraningDoc/')
        resolver_match = resolve('/TraningDoc/')
        self.assertEqual(resolver_match.func, views.register)


# def test_posts_url(self):
#     url = reverse('blog-CreatPost')
#     self.assertEqual(url, '/CreatPost/')
#     resolver_match = resolve('/CreatPost/')
#     self.assertEqual(resolver_match.func, views.CreatPost)




# -------------------- 04/01/2022 - unittest --------------

# ---- 1st try ---
"""
This test case will send a GET request to each of the URL patterns and check that the response has a status code of 200,
which indicates that the request was successful.
"""

class UrlsTestCase2(TestCase):
    def test_url_patterns(self):
        # Test the URL pattern for the 'blog-register' view
        url = reverse('blog-register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-community' view
        url = reverse('blog-community')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-admin' view
        url = reverse('blog-admin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-login' view
        url = reverse('blog-login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-HomePage' view
        url = reverse('blog-HomePage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-organization' view
        url = reverse('blog-organization')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-CreatEvent' view
        url = reverse('blog-CreatEvent')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-CreatMission' view
        url = reverse('blog-CreatMission')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-AllDocOrg' view
        url = reverse('blog-AllDocOrg')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-missions' view
        url = reverse('blog-missions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-AllDocAdm' view
        url = reverse('blog-AllDocAdm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-ComUserPage' view
        url = reverse('blog-ComUserPage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-CreatPost' view
        url = reverse('blog-CreatPost')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-OrgUserPage' view
        url = reverse('blog-OrgUserPage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-deleteUsers' view
        url = reverse('blog-deleteUsers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-UserAuth' view
        url = reverse('blog-UserAuth')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-PostAuth' view
        url = reverse('blog-PostAuth')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-ComUserPage' view
        url = reverse('blog-ComUserPage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-TrainingRating' view
        url = reverse('blog-TrainingRating')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-ActivityReport' view
        url = reverse('blog-ActivityReport')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-TraningDoc' view
        url = reverse('blog-TraningDoc')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test the URL pattern for the 'blog-AllDocCom' view
        url = reverse('blog-AllDocCom')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



                            # --- 2nd try ----

"""

To create a unit test for these URL patterns in your Django project that uses both the reverse and resolve functions,
you can do the following:
   Use the reverse function to get the URL for each pattern.
   Use the resolve function to check that the correct view function is being called for each URL.
"""

class UrlsTestCase1(TestCase):
    def test_url_patterns(self):
        # Test the URL pattern for the 'blog-register' view
        url = reverse('blog-register')
        self.assertEqual(resolve(url).view_name, 'blog-register')

        # Test the URL pattern for the 'blog-community' view
        url = reverse('blog-community')
        self.assertEqual(resolve(url).view_name, 'blog-community')

        # Test the URL pattern for the 'blog-admin' view
        url = reverse('blog-admin')
        self.assertEqual(resolve(url).view_name, 'blog-admin')

        # Test the URL pattern for the 'blog-login' view
        url = reverse('blog-login')
        self.assertEqual(resolve(url).view_name, 'blog-login')

        # Test the URL pattern for the 'blog-HomePage' view
        url = reverse('blog-HomePage')
        self.assertEqual(resolve(url).view_name, 'blog-HomePage')

        # Test the URL pattern for the 'blog-organization' view
        url = reverse('blog-organization')
        self.assertEqual(resolve(url).view_name, 'blog-organization')

        # Test the URL pattern for the 'blog-CreatEvent' view
        url = reverse('blog-CreatEvent')
        self.assertEqual(resolve(url).view_name, 'blog-CreatEvent')

        # Test the URL pattern for the 'blog-CreatMission' view
        url = reverse('blog-CreatMission')
        self.assertEqual(resolve(url).view_name, 'blog-CreatMission')

        # Test the URL pattern for the 'blog-AllDocOrg' view
        url = reverse('blog-AllDocOrg')
        self.assertEqual(resolve(url).view_name, 'blog-AllDocOrg')

        # Test the URL pattern for the 'blog-missions' view
        url = reverse('blog-missions')
        self.assertEqual(resolve(url).view_name, 'blog-missions')

        # Test the URL pattern for the 'blog-AllDocAdm' view
        url = reverse('blog-AllDocAdm')
        self.assertEqual(resolve(url).view_name, 'blog-AllDocAdm')

        # Test the URL pattern for the 'blog-ComUserPage' view
        url = reverse('blog-ComUserPage')
        self.assertEqual(resolve(url).view_name, 'blog-ComUserPage')

        # Test the URL pattern for the 'blog-CreatPost' view
        url = reverse('blog-CreatPost')
        self.assertEqual(resolve(url).view_name, 'blog-CreatPost')

        # Test the URL pattern for the 'blog-OrgUserPage' view
        url = reverse('blog-OrgUserPage')
        self.assertEqual(resolve(url).view_name, 'blog-OrgUserPage')

        # Test the URL pattern for the 'blog-deleteUsers' view
        url = reverse('blog-deleteUsers')
        self.assertEqual(resolve(url).view_name, 'blog-deleteUsers')

        # Test the URL pattern for the 'blog-UserAuth' view
        url = reverse('blog-UserAuth')
        self.assertEqual(resolve(url).view_name, 'blog-UserAuth')

        # Test the URL pattern for the 'blog-PostAuth' view
        url = reverse('blog-PostAuth')
        self.assertEqual(resolve(url).view_name, 'blog-PostAuth')

        # Test the URL pattern for the 'blog-ComUserPage' view
        url = reverse('blog-ComUserPage')
        self.assertEqual(resolve(url).view_name, 'blog-ComUserPage')

        # Test the URL pattern for the 'blog-TrainingRating' view
        url = reverse('blog-TrainingRating')
        self.assertEqual(resolve(url).view_name, 'blog-TrainingRating')

        # Test the URL pattern for the 'blog-ActivityReport' view
        url = reverse('blog-ActivityReport')
        self.assertEqual(resolve(url).view_name, 'blog-ActivityReport')

