import unittest
import requests

from selenium import webdriver

class TestSelenium(unittest.TestCase):  
  def setUp(self):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")

    self.browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)


  def test_search_homepage(self):
    browser = self.browser
    browser.get('https://radii.devinpeace.com')
    self.assertIn("Radii - Find your radius", browser.title)
    search = browser.find_element_by_id('search-input')
    search.send_keys("party")
    search_button = browser.find_element_by_id('search-button')
    search_button.click()
    browser.close()
  
  def test_display_event(self):
    browser = self.browser
    browser.get('https://radii.devinpeace.com/event')
    tag_name = browser.find_elements_by_class_name('services')
    self.assertEqual(77, len(tag_name))
  

