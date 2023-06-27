from ..locators.tasks_page_locators import TasksPageLocators, TaskFormLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TasksPage:

    def __init__(self, driver):
        self.driver = driver

    def get_btn_add_task(self):
        return self.driver.find_element(*TasksPageLocators.BTN_ADD_TASK)

    def wait_for_btn_add_task(self, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(TasksPageLocators.BTN_ADD_TASK))

    def wait_for_task_form(self, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(TaskFormLocators.TASK_FORM))

    def get_fld_title(self):
        return self.driver.find_element(*TaskFormLocators.FLD_TITLE)

    def get_fld_description(self):
        return self.driver.find_element(*TaskFormLocators.FLD_DESCRIPTION)

    def get_fld_environment(self):
        return self.driver.find_element(*TaskFormLocators.FLD_ENVIRONMENT)

    def get_fld_version(self):
        return self.driver.find_element(*TaskFormLocators.FLD_VERSION)

    def get_fld_date(self):
        return self.driver.find_element(*TaskFormLocators.FLD_DATE)

    def get_fld_assign(self):
        return self.driver.find_element(*TaskFormLocators.FLD_ASSIGN)

    def get_btn_save(self):
        return self.driver.find_element(*TaskFormLocators.BTN_SAVE)

    def get_btn_cancel(self):
        return self.driver.find_element(*TaskFormLocators.BTN_CANCEL)

    def wait_for_msg_success(self, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(TaskFormLocators.MSG_SUCCESS))

    def get_msg_success(self):
        return self.driver.find_element(*TaskFormLocators.MSG_SUCCESS)
