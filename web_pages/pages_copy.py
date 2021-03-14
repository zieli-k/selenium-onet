from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver


class BasePage(object):
    def __init__(self,driver: webdriver):
        self.driver = driver
        self.timeout = 15
        self.highlight = True


class MainPage(BasePage, PageFactory):
    locators = {'about_btn':  ('ID', 'about'),
                'python_logo': ('XPATH', '//img[@class="python-logo"]')}

    def click_about(self):
        self.about_btn.click_button()

    def is_logo_exist(self):
        return self.python_logo.is_displayed()


class AboutPage(BasePage, PageFactory):
    locators = {'about_banner': ('XPATH', '//div[@class="about-banner"]')}

    def get_about_banner_text(self):
        return self.about_banner.get_text()
