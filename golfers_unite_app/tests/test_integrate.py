from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from django.contrib.auth.mopdels import User
from golfers_unit_app import Golfer, Scorecard


from selenium import webdriver
from selenium.webdrvier.firefox.service import Service as Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

broswer = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

broswer.get('https://www.selenium.dev/documentation/')
assert 'selenium' in browser.title

elem = browser.find_element(By.NAME, 'p')
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()