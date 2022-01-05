from selenium.webdriver.common.by import By

class BasePageLocators():
    TEXT_AREA = (By.XPATH, "//*[@id='textbox']")
    PHRASE_AREA = (By.XPATH, "//*[@class = 'dailyPhrase-cardContent']/*[normalize-space(text())='Фраза дня'][1]")
    ICON_LOGIN = (By.XPATH, "//*[@id='userButton']")
    AREA_LANGUAGE = (By.XPATH, "//*[@id = 'fakeArea']")
    AREA_TRANSLATION = (By.XPATH, "//*[@id='translation']")
    TEXT_TRANSLATION = (By.XPATH, "//*[@id='translation']/span/span")
    BTN_LOGIN = (By.XPATH, "//*[@class='userMenu-addUser-title' and normalize-space(text())='Войти']")
    ICON_LOGIN_IN = (By.XPATH, "//*[@id='userButton']")

class AutHPageLocators():
    EMAIL = (By.XPATH, "//*[@id = 'passp-field-login']")
    PASSWORD = (By.XPATH, "//*[@id = 'passp-field-passwd']")
    LOG_IN_BTN = (By.XPATH, "//*[@id = 'passp:sign-in']")