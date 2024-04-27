from django.test import TestCase
from golfers_unite_app.forms import ScoreForm, LoginForm

class FormsTestCase(TestCase):
    # Your existing test cases...

    def test_score_form_valid(self):
        form_data = {
            'hole_number': 1,
            'par': 4,
            'distance': 400,
            'swing_score': 5
        }
        form = ScoreForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_score_form_invalid(self):
        form_data = {
            'hole_number': 1,
            'par': -1,  # Negative par
            'distance': 400,
            'swing_score': 5
        }
        form = ScoreForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_login_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'password': ''  # Empty password
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
