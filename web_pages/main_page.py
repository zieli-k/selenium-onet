from seleniumpagefactory.Pagefactory import PageFactory

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