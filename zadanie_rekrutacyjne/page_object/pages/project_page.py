from ..locators.project_page_locators import ProjectPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_btn_add_attachment(self, time):
        expected = EC.presence_of_element_located(ProjectPageLocators.BTN_ADD_ATTACHMENT)
        return WebDriverWait(self.driver, time).until(expected)

    def get_btn_add_attachment(self):
        return self.driver.find_element(*ProjectPageLocators.BTN_ADD_ATTACHMENT)

    def wait_for_btn_add_plan(self, time):
        expected = EC.presence_of_element_located(ProjectPageLocators.BTN_ADD_PLAN)
        return WebDriverWait(self.driver, time).until(expected)

    def get_btn_add_plan(self):
        return self.driver.find_element(*ProjectPageLocators.BTN_ADD_PLAN)
