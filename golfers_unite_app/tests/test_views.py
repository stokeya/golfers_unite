from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from golfers_unite_app.models import Golfer, Scorecard
from golfers_unite_app.views import *

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        # Create a golfer profile for the test user
        self.golfer = Golfer.objects.create(user=self.user, age=30)
        # Create a test scorecard
        self.scorecard = Scorecard.objects.create(golfer=self.golfer, date_played='2022-04-28', course_name='Test Course', score=72, par=72, holes=18)

    def test_index_view(self):
        # Test index view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'golfers_unite_app/index.html')

    def test_signup_view(self):
        # Test signup view with GET request
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'golfers_unite_app/signup.html')

        # Test signup view with POST request
        response = self.client.post(reverse('signup'), {'username': 'testuser2', 'email': 'test2@example.com', 'password1': 'testpassword', 'password2': 'testpassword', 'age': 25})
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_login_view(self):
        # Test login view with GET request
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'golfers_unite_app/login.html')

        # Test login view with POST request
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_welcome_view(self):
        # Login as the test user
        self.client.login(username='testuser', password='testpassword')
        # Test welcome view
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'golfers_unite_app/welcome.html')

    def test_active_golfers_view(self):
        # Test active golfers view
        response = self.client.get(reverse('active_golfers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'golfers_unite_app/active_golfers.html')

    def test_add_scorecard_view(self):
        # Login as the test user
        self.client.login(username='testuser', password='testpassword')
        # Test add scorecard view with GET request
        response = self.client.get(reverse('add_scorecard', kwargs={'golfer_id': self.golfer.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'golfers_unite_app/add_scorecard.html')

        # Test add scorecard view with POST request
        response = self.client.post(reverse('add_scorecard', kwargs={'golfer_id': self.golfer.id}), {'date_played': '2022-04-29', 'course_name': 'New Course', 'score': 75, 'par': 72, 'holes': 18})
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_edit_scorecard_view(self):
        # Login as the test user
        self.client.login(username='testuser', password='testpassword')
        # Test edit scorecard view with GET request
        response = self.client.get(reverse('edit_scorecard', kwargs={'scorecard_id': self.scorecard.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'golfers_unite_app/edit_scorecard.html')

        # Test edit scorecard view with POST request
        response = self.client.post(reverse('edit_scorecard', kwargs={'scorecard_id': self.scorecard.id}), {'date_played': '2022-04-30', 'course_name': 'Updated Course', 'score': 73, 'par': 72, 'holes': 18})
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_delete_scorecard_view(self):
        # Login as the test user
        self.client.login(username='testuser', password='testpassword')
        # Test delete scorecard view with POST request
        response = self.client.post(reverse('delete_scorecard', kwargs={'scorecard_id': self.scorecard.id}))
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_logout_view(self):
        # Test logout view with GET request
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect status code

