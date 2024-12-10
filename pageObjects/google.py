from selenium.webdriver.common.by import By


class GoogleSearch:
    def __init__(self, driver):
        self.driver = driver

    search = (By.XPATH, "//div/textarea[@id='APjFqb']")

    def search_action(self):
        return self.driver.find_element(*GoogleSearch.search)
