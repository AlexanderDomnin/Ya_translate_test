#Тесты на главной странице сайта
#from .pages.main_page import MainPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
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
