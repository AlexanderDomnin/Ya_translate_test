#Тесты на главной странице сайта
#from .pages.main_page import MainPage
from .pages.main_page import MainPage
import pytest
import allure

#Проверка элементов на главной странице сайта
@allure.feature('test_should_all_elements_main_page')
@allure.story('Проверка элементов на главной странице сайта')
def test_should_all_elements_main_page(browser):
    link = 'https://translate.yandex.ru/'
    with allure.step("Проверяем что есть основные элементы на странице'"):
        page = MainPage(browser,link)
        page.open()
        page.elements_main_page_correct()