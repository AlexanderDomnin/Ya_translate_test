from .base_page import BasePage
from .locators import BasePageLocators

class ProductPage(BasePage):
    def elements_main_page_correct(self):
        assert self.is_element_present(*BasePageLocators.TEXT_AREA), "No text area for translate"
        assert self.is_element_present(*BasePageLocators.PHRASE_AREA), "No phrase area for translate"
        assert self.is_element_present(*BasePageLocators.ICON_LOGIN), "No ICON for LOGIN on main page"

    def text_in_translate(self):
        self.browser.find_element(*BasePageLocators.AREA_LANGUAGE).send_keys('Test')

    def translate_is_correct(self):
        assert self.is_element_present(*BasePageLocators.AREA_TRANSLATION),"Translation form is not presented"
        assert 'Тест' in self.is_element_present(*BasePageLocators.TEXT_TRANSLATION).text, f"expected Translation to be 'Тест'"

    def auth_login(self):
        self.browser.find_element(*BasePageLocators.ICON_LOGIN).click()
        self.browser.find_element(*BasePageLocators.BTN_LOGIN).click()
        assert 'https://passport.yandex.ru/auth' in self.browser.current_url,f"expected login to be substring of '{self.browser.current_url}'"

    def auth_login_page(self):
        assert 'https://translate.yandex.ru/' == self.browser.current_url, f"expected login to be substring of '{self.browser.current_url}'"
        assert self.is_element_present(*BasePageLocators.ICON_LOGIN), "No ICON for LOGIN on main page"


