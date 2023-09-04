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
    

    # def test_instructorSearch(self):
    #     self.selenium.get('https://b07-scheduler.herokuapp.com/search/class')
    #     time.sleep(1)
    #     department = self.selenium.find_element(By.XPATH, '//*[@id="subject"]/option[46]')
    #     department.click()
    #     time.sleep(1)
    #     classSearch = self.selenium.find_element(By.NAME,"catalog_nbr")
    #     classSearch.send_keys('4435')
    #     time.sleep(1)
    #     search = self.selenium.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[4]/button')
    #     search.click()
    #     assert 'Computer Architecture & Design' in self.selenium.page_source