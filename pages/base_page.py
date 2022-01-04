from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def elements_main_page_correct(self):
        assert self.is_element_present(*BasePageLocators.TEXT_AREA), "No text area for translate"
        assert self.is_element_present(*BasePageLocators.PHRASE_AREA), "No phrase area for translate"
        assert self.is_element_present(*BasePageLocators.ICON_LOGIN), "No ICON for LOGIN on main page"

