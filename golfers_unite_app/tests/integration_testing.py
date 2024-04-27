from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from django.contrib.auth.models import User
from golfers_unite_app import *

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

browser.get('localhost:8000')

class GolfersUniteIntegrationTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  # Use appropriate WebDriver here
        cls.selenium.implicitly_wait(10)   # Adjust as needed

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # Navigate to the login page
        self.selenium.get(self.live_server_url + '/login/')
        # Fill in login form
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('testpassword')
        # Submit the form
        login_button = self.selenium.find_element_by_css_selector('button[type="submit"]')
        login_button.click()
        # Assert that the user is redirected to the expected page after login
        self.assertEqual(self.selenium.current_url, self.live_server_url + '/welcome/')

    def test_add_scorecard(self):
        # Navigate to the page where you can add a scorecard
        self.selenium.get(self.live_server_url + '/add_scorecard/')
        # Fill in the form to add a scorecard
        # (you'll need to identify form elements and fill them out similar to the signup test)
        # Submit the form
        add_scorecard_button = self.selenium.find_element_by_css_selector('button[type="submit"]')
        add_scorecard_button.click()
        # Assert that the user is redirected to the expected page after adding a scorecard
        self.assertEqual(self.selenium.current_url, self.live_server_url + '/active_golfers/')

    def test_edit_scorecard(self):
        # Navigate to the page where you can edit a scorecard
        # (you'll need to navigate to a specific scorecard's edit page)
        self.selenium.get(self.live_server_url + '/edit_scorecard/1/')  # Example URL, adjust as needed
        # Fill in the form to edit the scorecard
        # (you'll need to identify form elements and fill them out similar to the add_scorecard test)
        # Submit the form
        edit_scorecard_button = self.selenium.find_element_by_css_selector('button[type="submit"]')
        edit_scorecard_button.click()
        # Assert that the user is redirected to the expected page after editing the scorecard
        self.assertEqual(self.selenium.current_url, self.live_server_url + '/active_golfers/')

    def test_delete_scorecard(self):
        # Navigate to the page where you can delete a scorecard
        # (you'll need to navigate to a specific scorecard's delete page)
        self.selenium.get(self.live_server_url + '/delete_scorecard/1/')  # Example URL, adjust as needed
        # Confirm deletion (you may need to locate and click on a confirmation button)
        confirm_delete_button = self.selenium.find_element_by_css_selector('button[type="submit"]')
        confirm_delete_button.click()
        # Assert that the user is redirected to the expected page after deleting the scorecard
        self.assertEqual(self.selenium.current_url, self.live_server_url + '/active_golfers/')
