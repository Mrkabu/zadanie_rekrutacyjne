from selenium.webdriver.common.by import By


class MenuBarLocators:

    MENU = (By.CLASS_NAME, "menu")

    # buttons
    BTN_KOKPIT = (By.LINK_TEXT, "Kokpit")
    BTN_PROJEKT = (By.LINK_TEXT, "Projekt")
    BTN_WYDANIA = (By.LINK_TEXT, "Wydania")
    BTN_SRODOWISKA = (By.LINK_TEXT, "Środowiska")
    BTN_WERSJE = (By.LINK_TEXT, "Wersje")
    BTN_TAGI = (By.LINK_TEXT, "Tagi")
    BTN_ZADANIA = (By.LINK_TEXT, "Zadania")
    BTN_DEFEKTY = (By.LINK_TEXT, "Defekty")
    BTN_BAZA_TESTOW = (By.LINK_TEXT, "Baza testów")
    BTN_PLIKI = (By.LINK_TEXT, "Pliki")
