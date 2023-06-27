import pytest
from web_driver_setup import WebDriverSetup
from common.test_login import login
from page_object.pages.menu_bar import MenuBar
from page_object.pages.tasks_page import TasksPage
from selenium.webdriver.common.keys import Keys
import time

driver = WebDriverSetup().driver


class TestAddTask:

    def test_before(self):
        login(driver)

    def test_add_task(self):
        # choose tasks from the menu
        menu = MenuBar(driver)
        menu.wait_for_menu(5)
        menu.get_btn_zadania().click()

        # open new task form
        tasks = TasksPage(driver)
        tasks.wait_for_btn_add_task(5)
        tasks.get_btn_add_task().click()
        tasks.wait_for_task_form(5)

        # fill the task form
        tasks.get_fld_title().clear()
        tasks.get_fld_title().send_keys('aaaaaaaaaaaaaaa')
        tasks.get_fld_description().clear()
        tasks.get_fld_description().send_keys('descriptiondescriptiondescriptiondescriptiondescription')
        tasks.get_fld_environment().clear()
        tasks.get_fld_environment().send_keys('dev')
        time.sleep(1)
        tasks.get_fld_environment().send_keys(Keys.ENTER)
        tasks.get_fld_version().clear()
        tasks.get_fld_version().send_keys('ver')
        time.sleep(1)
        tasks.get_fld_version().send_keys(Keys.ENTER)
        tasks.get_fld_date().clear()
        tasks.get_fld_date().send_keys('2023-08-01 23:59')
        tasks.get_fld_assign().click()

        # save the form
        tasks.get_btn_save().click()

        # verify that the task was created
        tasks.wait_for_msg_success(5)

    def test_after(self):
        driver.quit()
