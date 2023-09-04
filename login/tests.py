#from django.test import TestCase

# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.webdriver import WebDriver

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MySeleniumTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_home_page_loads(self):
        self.selenium.get('https://b07-scheduler.herokuapp.com/')
        assert 'BTS (Better Than SIS) Scheduler' in self.selenium.page_source

    # def test_student_login_button(self):
    #     self.selenium.get('https://b07-scheduler.herokuapp.com/')
    #     student_login = self.selenium.find_element(By.XPATH,'/html/body/div[4]/main/div/div/div[1]/form/button')
    #     student_login.click()
    #     assert 'Sign in with Google' in self.selenium.page_source

    # def test_home_navBar(self):
    #     self.selenium.get('%s%s' % (self.live_server_url, '/login/profile/'))
    #     home = self.selenium.find_element(By.LINK_TEXT,"Home")
    #     home.click()
    #     assert 'BTS (Better Than SIS) Scheduler' in self.selenium.page_source

    def test_scheduleTools_navBar(self):
        self.selenium.get('https://b07-scheduler.herokuapp.com/tools/')
        assert 'Cart' in self.selenium.page_source

    def test_myProfile_navBar(self):
        self.selenium.get('https://b07-scheduler.herokuapp.com/login/profile/')
        assert 'Student Profile' in self.selenium.page_source
    