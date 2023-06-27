from selenium.webdriver.common.by import By


class FileBrowserPageLocators:

    # fields
    FLD_DIR_NAME = (By.ID, 'directoryName')

    # buttons
    BTN_CREATE_DIR = (By.ID, 'createDirectoryButton')

    # dirs
    DIR_NAME = (By.XPATH, '//a[@path=\"|{text}\"]')
