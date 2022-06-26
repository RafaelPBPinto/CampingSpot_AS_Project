from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create your tests here.

class PlayerFromTest(LiveServerTestCase):

    def testSearch(self):
        selenium = webdriver.Chrome()

        selenium.get('https://campingspot.herokuapp.com/')

        search = selenium.find_element(By.ID,"searched")

        submit = selenium.find_element(By.ID,"submit")

        search.send_keys('Madeira')

        submit.send_keys(Keys.RETURN)

        assert 'Madeira' in selenium.page_source

