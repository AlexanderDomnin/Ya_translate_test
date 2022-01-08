from .pages.main_page import MainPage
from .pages.site_page import SitePage
import pytest
import allure

@allure.feature('Работа вкладки сайты')
#@pytest.mark.xfail
def test_translation_sites_work_is_correct(browser):
    link = 'https://translate.yandex.ru/'
    with allure.step("Открыть главную страницу"):
        page = MainPage(browser, link)
        page.open()
    with allure.step("Открыть вкладку сайты"):
        site_page = SitePage(browser, browser.current_url)
        site_page.click_on_sitepage()
        site_page.url_should_correct_on_site_page()
    with allure.step("Проверить элементы вкладки сайты"):
        site_page.site_page_with_translate_correct_blocks()
    with allure.step("Добавить сайт для перевода"):
        site_page.site_for_translate()
    with allure.step("Проверить перевод сайта"):
        site_page.site_after_translate()

