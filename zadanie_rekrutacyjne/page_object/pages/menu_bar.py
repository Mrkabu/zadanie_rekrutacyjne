from ..locators.menu_bar_locators import MenuBarLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuBar:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_menu(self, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(MenuBarLocators.MENU))

    def get_btn_kokpit(self):
        return self.driver.find_element(*MenuBarLocators.BTN_KOKPIT)

    def get_btn_projekt(self):
        return self.driver.find_element(*MenuBarLocators.BTN_PROJEKT)

    def get_btn_wydania(self):
        return self.driver.find_element(*MenuBarLocators.BTN_WYDANIA)

    def get_btn_srodowiska(self):
        return self.driver.find_element(*MenuBarLocators.BTN_SRODOWISKA)

    def get_btn_wersje(self):
        return self.driver.find_element(*MenuBarLocators.BTN_WERSJE)

    def get_btn_tagi(self):
        return self.driver.find_element(*MenuBarLocators.BTN_TAGI)

    def get_btn_zadania(self):
        return self.driver.find_element(*MenuBarLocators.BTN_ZADANIA)

    def get_btn_defekty(self):
        return self.driver.find_element(*MenuBarLocators.BTN_DEFEKTY)

    def get_btn_baza_testow(self):
        return self.driver.find_element(*MenuBarLocators.BTN_BAZA_TESTOW)

    def get_btn_pliki(self):
        return self.driver.find_element(*MenuBarLocators.BTN_PLIKI)

