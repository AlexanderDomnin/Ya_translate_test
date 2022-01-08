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
    SRC_LANG = (By.XPATH, "//*[@id='srcLangButton']")
    DST_LANG = (By.XPATH, "//*[@id = 'dstLangButton']")
    EXAMPLE_BLOCK = (By.XPATH, "//*[@id = 'examples']")
    DICT_BLOCK = (By.XPATH, "//*[@id = 'dictionary']")
    RELATIVE_BLOCK = (By.XPATH, "//*[@id = 'relatedWords']")
    DECL_BLOCK = (By.XPATH, "//*[@id = 'declensions']")
    FOOTER_BLOCK = (By.XPATH, "//*[@class = 'footer-links']")
    HISTORY_BLOCK = (By.XPATH, "//*[@id = 'historyRecent']")
    HIST_TRANSLATE = (By.XPATH, "//*[@class = 'history_records-item-text']")

class AutHPageLocators():
    EMAIL = (By.XPATH, "//*[@id = 'passp-field-login']")
    PASSWORD = (By.XPATH, "//*[@id = 'passp-field-passwd']")
    LOG_IN_BTN = (By.XPATH, "//*[@id = 'passp:sign-in']")

class SitePageLocators():
    HEAD_LINK_SITE = (By.XPATH, "//a[@href='/translate']")
    SRC_LANG_SITE = (By.XPATH, "//*[@id='srcLangButton']")
    DST_LANG_SITE = (By.XPATH, "//*[@id = 'dstLangButton']")
    SWAP_LANG = (By.XPATH, "//*[@class='langs-swapButton']")
    INPUT_FOR_URL = (By.XPATH, "//*[@id = 'urlInput-input']")
    BTN_FOR_URL = (By.XPATH, "//*[@id = 'urlInput-button']")
    TR_SITE_INPUT = (By.XPATH, "//*[@id = 'urlTrInput-input']")
    PROGRESS_TR = (By.XPATH, "//*[@id = 'progress' and normalize-space(text())='100%']")
    PAGE_TR = (By.XPATH, "//span[@class = 'button__text']/*[@data-value = 'Найти' and @data-translation = 'To find']")