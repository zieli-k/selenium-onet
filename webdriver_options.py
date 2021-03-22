from selenium.webdriver.chrome.options import Options


class WebdriverOptions():
    def __init__(self):
        self.list_of_options = ["start-maximized", "incognito"]
        self.options = Options()
        for option in self.list_of_options:
            self.options.add_argument(option)
