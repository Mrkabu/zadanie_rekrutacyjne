from ..locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login = 'administrator@testarena.pl'
        self.password = 'sumXQQ72$L'

    def get_fld_email(self):
        return self.driver.find_element(*LoginPageLocators.FLD_EMAIL)

    def get_fld_password(self):
        return self.driver.find_element(*LoginPageLocators.FLD_PASSWORD)

    def get_btn_login(self):
        return self.driver.find_element(*LoginPageLocators.BTN_LOGIN)

    def get_err_login(self):
        return self.driver.find_element(*LoginPageLocators.ERR_LOGIN)

    def wait_for_err_login(self, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(LoginPageLocators.ERR_LOGIN))
