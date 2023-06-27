import pytest
from web_driver_setup import WebDriverSetup
from page_object.pages.demo_page import DemoPage
from page_object.pages.login_page import LoginPage

driver = WebDriverSetup().driver


class TestLoginIncorrectCredentials:
    
    def test_before(self):
        driver.get('http://testarena.pl/demo')
        demo_page = DemoPage(driver)
        demo_page.get_btn_demo().click()
        driver.switch_to.window(driver.window_handles[1])

    def test_incorrect_email_login(self):
        """Logging into the service using incorrect email should result in error message"""
        login_page = LoginPage(driver)
    
        # send incorrect email
        login_page.get_fld_email().clear()
        login_page.get_fld_email().send_keys('aaa', login_page.login)
    
        # send correct password
        login_page.get_fld_password().clear()
        login_page.get_fld_password().send_keys(login_page.password)
    
        # try to log in
        login_page.get_btn_login().click()
    
        # login results in error
        login_page.wait_for_err_login(5)
        error_message = login_page.get_err_login().text
        assert error_message == "Adres e-mail i/lub hasło są niepoprawne."
    
    def test_incorrect_password_login(self):
        """Logging into the service using incorrect password should result in error message"""
        login_page = LoginPage(driver)

        # send correct email
        login_page.get_fld_email().clear()
        login_page.get_fld_email().send_keys(login_page.login)

        # send incorrect password
        login_page.get_fld_password().clear()
        login_page.get_fld_password().send_keys('123', login_page.password)

        # try to log in
        login_page.get_btn_login().click()

        # login results in error
        login_page.wait_for_err_login(5)
        error_message = login_page.get_err_login().text
        assert error_message == "Adres e-mail i/lub hasło są niepoprawne."

    def test_after(self):
        driver.quit()
