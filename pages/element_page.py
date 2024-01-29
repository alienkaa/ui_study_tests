import time

from locators.elements_page_locators import PageLocators
from pages.base_page import BasePage


class TextLocators(BasePage):
    locators = PageLocators()

    def fill_of_fields(self):
        self.elem_is_visible(self.locators.FULL_NANE).send_keys('Ivan Petrov')
        self.elem_is_visible(self.locators.EMAIL).send_keys("gmail@mail.com")
        self.elem_is_visible(self.locators.CURRENT_ADDRESS).send_keys('15 Quantock Rd')
        self.elem_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Weston-super-Mare BS23 1HL')
        self.elem_is_visible(self.locators.SUBMIT).click()
        time.sleep(4)
