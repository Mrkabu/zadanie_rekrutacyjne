from page_object.pages.demo_page import DemoPage
from page_object.pages.login_page import LoginPage


def login(driver):
    driver.get('http://testarena.pl/demo')
    demo_page = DemoPage(driver)
    demo_page.get_btn_demo().click()
    driver.switch_to.window(driver.window_handles[1])

    # log into the service
    login_page = LoginPage(driver)
    login_page.get_fld_email().clear()
    login_page.get_fld_email().send_keys(login_page.login)
    login_page.get_fld_password().clear()
    login_page.get_fld_password().send_keys(login_page.password)
    login_page.get_btn_login().click()
