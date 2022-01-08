from .base_page import BasePage
from .locators import SitePageLocators

class SitePage(BasePage):
    def click_on_sitepage(self):
        self.browser.find_element(*SitePageLocators.HEAD_LINK_SITE).click()

    def url_should_correct_on_site_page(self):
        assert 'https://translate.yandex.ru/translate' == self.browser.current_url, f"Site page not correct - '{self.browser.current_url}'"

    def site_page_with_translate_correct_blocks(self):
        assert self.is_element_present(*SitePageLocators.SRC_LANG_SITE), "NO SRC_LANG_SITE on page"
        assert self.is_element_present(*SitePageLocators.DST_LANG_SITE), "NO DST_LANG_SITE on page"
        assert self.is_element_present(*SitePageLocators.SWAP_LANG), "NO SWAP_LANG on page"
        assert self.is_element_present(*SitePageLocators.INPUT_FOR_URL), "NO INPUT_FOR_URL on page"

    def site_for_translate(self):
        self.browser.find_element(*SitePageLocators.INPUT_FOR_URL).send_keys('ya.ru')
        self.browser.find_element(*SitePageLocators.BTN_FOR_URL).click()

    def site_after_translate(self):
        assert 'https://ya.ru/' == self.browser.find_element(*SitePageLocators.TR_SITE_INPUT).text, f"URL SITE not correct - {self.browser.find_element(*SitePageLocators.TR_SITE_INPUT).text}"
        assert self.is_element_present(*SitePageLocators.PROGRESS_TR), "NO Progress translation on page"
        assert self.is_element_present(*SitePageLocators.PAGE_TR), "NO Page translation on page"
