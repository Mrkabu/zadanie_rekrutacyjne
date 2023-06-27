from selenium.webdriver.common.by import By


class TasksPageLocators:

    # buttons
    BTN_ADD_TASK = (By.XPATH, "//a[@href=\"http://demo.testarena.pl/DNSTES/task_add\"]")


class TaskFormLocators:

    # task form
    TASK_FORM = (By.XPATH, "//form[@action=\"http://demo.testarena.pl/DNSTES/task_add_process\"]")

    # fields
    FLD_TITLE = (By.ID, 'title')
    FLD_DESCRIPTION = (By.ID, 'description')
    FLD_ENVIRONMENT = (By.ID, 'token-input-environments')
    FLD_VERSION = (By.ID, 'token-input-versions')
    FLD_DATE = (By.ID, 'dueDate')
    FLD_ASSIGN = (By.ID, 'j_assignToMe')

    # buttons
    BTN_SAVE = (By.ID, 'save')
    BTN_CANCEL = (By.CLASS_NAME, 'j_cancel_button')

    # messages
    MSG_SUCCESS = (By.XPATH, "//div[@id=\"j_info_box\"]/p[text()=\"Zadanie zostało dodane.\"]")
