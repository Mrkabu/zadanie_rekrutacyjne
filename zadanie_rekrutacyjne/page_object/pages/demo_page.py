from ..locators.demo_page_locators import DemoPageLocators


class DemoPage:

    def __init__(self, driver):
        self.driver = driver

    def get_btn_demo(self):
        return self.driver.find_element(*DemoPageLocators.BTN_DEMO)

