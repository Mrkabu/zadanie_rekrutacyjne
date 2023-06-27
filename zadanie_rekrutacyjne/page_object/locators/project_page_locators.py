from selenium.webdriver.common.by import By


class ProjectPageLocators:

    # buttons
    BTN_ADD_ATTACHMENT = (By.XPATH, "//a[contains(text(), \"Dodaj załącznik\")]")
    BTN_ADD_PLAN = (By.ID, 'j_projectAddPlan')
