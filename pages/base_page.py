class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(5)

    def open(self):
        self.driver.get(self.url)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)