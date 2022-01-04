from selenium.webdriver.common.by import By

class BasePageLocators():
    TEXT_AREA = (By.XPATH, "//*[@id='textbox']")
    PHRASE_AREA = (By.XPATH, "//*[@class = 'dailyPhrase-cardContent']/*[normalize-space(text())='Фраза дня'][1]")
    ICON_LOGIN = (By.XPATH, "//*[@id='userButton']")
