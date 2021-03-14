from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
import unittest
from configuration.config import Url
import time
import sys
from webdriver_options import WebdriverOptions


class MainPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.highlight = True

    locators = {'about_btn':  ('ID', 'about'),
                'python_logo': ('XPATH', '//img[@class="python-logo"]')}

    def click_about(self):
        self.about_btn.click_button()

    def is_logo_exist(self):
        return self.python_logo.is_displayed()


class MainPageTest(unittest.TestCase):
    def setUp(self):
        options = WebdriverOptions().options
        self.driver = webdriver.Chrome(options=options)
        self.main_page = MainPage(self.driver)
        self.driver.get(Url(ENV).get_main_url())

    def test_main_page(self):
        self.driver.get(Url(ENV).get_main_url())
        assert self.main_page.is_logo_exist() == True
        self.main_page.click_about()
        self.driver.save_screenshot("screenshot.png")
        self.driver.quit()


if __name__ == "__main__":
    ENV = sys.argv[1]
    unittest.main(argv=['prod'])
