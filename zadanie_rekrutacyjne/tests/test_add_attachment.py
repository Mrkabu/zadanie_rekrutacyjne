import pytest
from web_driver_setup import WebDriverSetup
from common.test_login import login
from page_object.pages.menu_bar import MenuBar
from page_object.pages.project_page import ProjectPage
from page_object.pages.file_browser_page import FileBrowserPage
from selenium.webdriver.common.keys import Keys

driver = WebDriverSetup().driver


class TestAddAttachment:

    def test_before(self):
        login(driver)

    def test_add_attachment(self):
        # choose Project from the menu
        menu = MenuBar(driver)
        menu.wait_for_menu(5)
        menu.get_btn_projekt().click()

        # open attachment dropdown
        project = ProjectPage(driver)
        project.wait_for_btn_add_attachment(5)
        project.get_btn_add_attachment().click()
        project.wait_for_btn_add_plan(5)
        project.get_btn_add_plan().click()

        # add new directory to plan
        driver.switch_to.window(driver.window_handles[-1])
        browser = FileBrowserPage(driver)
        browser.wait_for_btn_create_dir(5)
        browser.get_btn_create_dir().click()
        browser.wait_for_fld_dir_name(5)
        browser.get_fld_dir_name().clear()
        browser.get_fld_dir_name().send_keys('testtesttest', Keys.ENTER)

        # verify that the new directory was added
        browser.wait_for_dir_name(5, 'testtesttest')

    def test_after(self):
        driver.quit()
