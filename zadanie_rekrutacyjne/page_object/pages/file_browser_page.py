from ..locators.file_browser_page_locators import FileBrowserPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FileBrowserPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_btn_create_dir(self, time):
        expected = EC.presence_of_element_located(FileBrowserPageLocators.BTN_CREATE_DIR)
        return WebDriverWait(self.driver, time).until(expected)

    def get_btn_create_dir(self):
        return self.driver.find_element(*FileBrowserPageLocators.BTN_CREATE_DIR)

    def wait_for_fld_dir_name(self, time):
        expected = EC.presence_of_element_located(FileBrowserPageLocators.FLD_DIR_NAME)
        return WebDriverWait(self.driver, time).until(expected)

    def get_fld_dir_name(self):
        return self.driver.find_element(*FileBrowserPageLocators.FLD_DIR_NAME)

    def wait_for_dir_name(self, time, text):
        expected = EC.presence_of_element_located((FileBrowserPageLocators.DIR_NAME[0],
                                                   FileBrowserPageLocators.DIR_NAME[1].format(text=text)))
        return WebDriverWait(self.driver, time).until(expected)
