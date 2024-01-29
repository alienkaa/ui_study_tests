import time
from pages.element_page import TextLocators
from conftest import driver
url = 'https://demoqa.com/text-box'


class TestTextBox:
    def test_text(self, driver):
        text_page = TextLocators(driver, url)
        text_page.open()
        text_page.fill_of_fields()
        time.sleep(5)
