from selenium.webdriver.common.keys import Keys

from pageObjects.google import GoogleSearch
from utilities.base_class import BaseClass


class Test(BaseClass):
    def test_negative(self):
        log = self.get_logger()
        google_search = GoogleSearch(self.driver)
        google_search.search_action().send_keys("Python"+Keys.ENTER)
        page_source = self.driver.page_source
        word_to_search = "java"
        assert word_to_search in page_source, f"'{word_to_search}' is NOT present on the page."

    def test_positive(self):
        log = self.get_logger()
        google_search = GoogleSearch(self.driver)
        google_search.search_action().send_keys("Python"+Keys.ENTER)
        page_source = self.driver.page_source
        word_to_search = "python"
        assert word_to_search in page_source, f"'{word_to_search}' is NOT present on the page."
