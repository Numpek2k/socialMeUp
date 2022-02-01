import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.opera.options import Options

PATH = "E:\operadriver\chromedriver.exe"

class full_test(LiveServerTestCase):

    def test_login(self):

        driver = webdriver.Chrome(PATH)

        driver.get('http://127.0.0.1:8000/')
        username = driver.find_element('name', 'username')
        password = driver.find_element('name', 'password')
        submit = driver.find_element('name', 'submit_button')

        time.sleep(3)

        username.send_keys('admin')
        password.send_keys('haslo')

        time.sleep(3)

        submit.send_keys(Keys.RETURN)

        time.sleep(3)

        assert 'Profile' in driver.page_source


