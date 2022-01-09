#Тесты на главной странице сайта
#from .pages.main_page import MainPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.site_page import SitePage
import pytest
import allure

#Проверка элементов на главной странице сайта
@allure.feature('test_should_all_elements_main_page')
@allure.story('Проверка элементов на главной странице сайта')
def test_should_all_elements_main_page(browser):
    link = 'https://translate.yandex.ru/'
    with allure.step("Проверяем что есть основные элементы на странице'"):
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.elements_main_page_correct()
    with allure.step("обновляем страницу и првоеряем элементы"):
        page.refresh()
        product_page.elements_main_page_correct()
    with allure.step("Добавить слово и проверить, что появился перевод"):
        product_page.text_in_translate()
        product_page.translate_is_correct()

#Проверка авторизации
@allure.feature('test_authtorization')
@allure.story('Проверка авторизации')
def test_authtorization(browser):
    link = 'https://translate.yandex.ru/'
    with allure.step("Открываем главную страницу и проверяем основные элементы'"):
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.elements_main_page_correct()
    with allure.step("Нажимаем на логин и проверяем корректность редиректа"):
        product_page.auth_login()
    with allure.step("Логин тестовым юзером"):
        page.auth_test_user()
    with allure.step('Проверка главной страницы после залогина'):
        product_page.auth_login_page()


#Проверка элементов на главной странице сайта, после перевода
@allure.feature('Проверка элементов на главной странице сайта c переводом')
@allure.story('Проверка элементов на главной странице сайта c переводом')
def test_should_all_elements_main_page_with_translate(browser):
    link = 'https://translate.yandex.ru/'
    with allure.step("Открыть главную страницу"):
        page = MainPage(browser, link)
        page.open()
        page.refresh()
    with allure.step("Добавить слово и проверить, что появился перевод"):
        product_page = ProductPage(browser, browser.current_url)
        product_page.text_in_translate()
        product_page.translate_is_correct()
    with allure.step("Проверить элементы страницы с переводом"):
        product_page.main_page_with_translate_correct_lang()
        product_page.main_page_with_translate_correct_blocks()
    with allure.step("Открыть другую вкладку и вернуться назад"):
        site_page = SitePage(browser,browser.current_url)
        site_page.click_on_sitepage()
        site_page.url_should_correct_on_site_page()
        site_page.go_back()
    with allure.step("Проверить, что на главной странице нет блоков с подсказками"):
        product_page.main_page_with_no_translate_correct_blocks()
    with allure.step("Ecть блок с последними переводами"):
        product_page.main_page_on_history_block()
