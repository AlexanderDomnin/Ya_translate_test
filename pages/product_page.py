from .base_page import BasePage
from .locators import BasePageLocators
import time
class ProductPage(BasePage):
    def elements_main_page_correct(self):
        assert self.is_element_present(*BasePageLocators.TEXT_AREA), "No text area for translate"
        assert self.is_element_present(*BasePageLocators.PHRASE_AREA), "No phrase area for translate"
        assert self.is_element_present(*BasePageLocators.ICON_LOGIN), "No ICON for LOGIN on main page"

    def text_in_translate(self):
        self.browser.find_element(*BasePageLocators.AREA_LANGUAGE).send_keys('Test')

    def translate_is_correct(self):
        assert self.is_element_present(*BasePageLocators.AREA_TRANSLATION),"Translation form is not presented"
        text_tr = self.browser.find_element(*BasePageLocators.TEXT_TRANSLATION).text
        assert text_tr == 'Тест', f"expected Translation to be {text_tr}"

    def auth_login(self):
        self.browser.find_element(*BasePageLocators.ICON_LOGIN).click()
        self.browser.find_element(*BasePageLocators.BTN_LOGIN).click()
        assert 'https://passport.yandex.ru/auth' in self.browser.current_url,f"expected login to be substring of '{self.browser.current_url}'"

    def auth_login_page(self):
        time.sleep(5)
        assert 'https://translate.yandex.ru/' == self.browser.current_url, f"expected https://translate.yandex.ru/ to be substring of '{self.browser.current_url}'"
        assert self.is_element_present(*BasePageLocators.ICON_LOGIN), "No ICON for LOGIN on main page"

    def main_page_with_translate_correct_lang(self):
        assert 'АНГЛИЙСКИЙ' == self.browser.find_element(*BasePageLocators.SRC_LANG).text, f"SRC translation is not correct - {self.browser.find_element(*BasePageLocators.SRC_LANG).text}"
        assert 'РУССКИЙ' == self.browser.find_element(*BasePageLocators.DST_LANG).text, "DST translation is not correct"

    def main_page_with_translate_correct_blocks(self):
        assert self.is_element_present(*BasePageLocators.EXAMPLE_BLOCK), "NO Example_block on page"
        assert self.is_element_present(*BasePageLocators.DICT_BLOCK), "NO DICT_BLOCK on page"
        assert self.is_element_present(*BasePageLocators.RELATIVE_BLOCK), "NO RELATIVE_BLOCK on page"
        assert self.is_element_present(*BasePageLocators.DECL_BLOCK), "NO DECL_BLOCK on page"
        assert self.is_element_present(*BasePageLocators.FOOTER_BLOCK), "NO FOOTER_BLOCK on page"

    def main_page_with_no_translate_correct_blocks(self):
        assert self.is_not_element_present(*BasePageLocators.EXAMPLE_BLOCK), "Example_block on page"
        assert self.is_not_element_present(*BasePageLocators.DICT_BLOCK), "DICT_BLOCK on page"
        assert self.is_not_element_present(*BasePageLocators.RELATIVE_BLOCK), "RELATIVE_BLOCK on page"
        assert self.is_not_element_present(*BasePageLocators.DECL_BLOCK), "DECL_BLOCK on page"

    def main_page_on_history_block(self):
        assert self.is_element_present(*BasePageLocators.HISTORY_BLOCK), "NO HISTORY_BLOCK on page"
        assert 'Test' == self.browser.find_element(*BasePageLocators.HIST_TRANSLATE).text, f"Not correct words in translate history - {self.browser.find_element(*BasePageLocators.HIST_TRANSLATE).text}"




