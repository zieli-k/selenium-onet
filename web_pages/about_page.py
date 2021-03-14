from seleniumpagefactory.Pagefactory import PageFactory

class AboutPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.highlight = True

    locators = { 'about_banner': ('XPATH', '//div[@class="about-banner"]')}

    def get_about_banner_text(self):
        return self.about_banner.get_text()