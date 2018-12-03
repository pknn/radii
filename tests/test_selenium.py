import unittest
from selenium import webdriver


class TestSelenium(unittest.TestCase):  
  def setUp(self):
    options = webdriver.ChromeOptions()
    self.browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)


  def test_event_invalid_url(self):
    browser = self.browser
    browser.get('https://radii.devinpeace.com/event')
    links = []
    tag_name = browser.find_elements_by_tag_name('a')
    for t in tag_name:
      links.append(t.get_attribute("href"))    
    invalid_links = []
    for l in links:    
      resp = requests.head(str(l))
      if resp.status_code != 200:
        invalid_links.append(l)    
    self.assertEqual(0, len(invalid_links))

  def test_login(self):
    browser = self.browser
    browser.get('https://radii.devinpeace.com')
    login_modal = browser.find_element_by_class_name('nav-link')
    login_modal.click()
    email = browser.find_element_by_name('email')
    password = browser.find_element_by_name('password')
    email[0].send_keys("test@example.com")
    password[0].send_keys("test1234")
    login_button = browser.find_element_by_id('loginbutton')
    login_button.click()
    
  def tearDown(self):
    self.browser.close()
  
  

