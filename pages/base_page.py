class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
