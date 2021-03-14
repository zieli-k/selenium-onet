from selenium import webdriver
import unittest
from configuration.config import Url
import sys
from webdriver_options import WebdriverOptions
from web_pages.pages_copy import MainPage, AboutPage


class MainPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=WebdriverOptions().options)
        self.main_page = MainPage(self.driver)
        self.url = Url(ENV).get_main_url()

    def test_main_page(self):
        try:
            self.driver.get(self.url)
            assert self.main_page.is_logo_exist() == True
        except AssertionError:
            self.driver.save_screenshot("main_page.png")
            raise Exception("Logo element doesn't exists")
        finally:
            self.driver.quit()


class AboutPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=WebdriverOptions().options)
        self.main_page = MainPage(self.driver)
        self.about_page = AboutPage(self.driver)
        self.url = Url(ENV).get_main_url()

    def test_about_page(self):
        try:
            self.driver.get(self.url)
            self.main_page.click_about()
            assert "Python is powerful" in self.about_page.get_about_banner_text()
        except AssertionError:
            self.driver.save_screenshot("about_page.png")
            raise Exception("Bad text or element doesn't exists")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    ENV = sys.argv[1]
    unittest.main(argv=['prod'])
