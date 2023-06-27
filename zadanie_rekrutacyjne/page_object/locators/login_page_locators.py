from selenium.webdriver.common.by import By


class LoginPageLocators:

    # fields
    FLD_EMAIL = (By.ID, 'email')
    FLD_PASSWORD = (By.ID, 'password')

    # buttons
    BTN_LOGIN = (By.ID, 'login')

    # errors
    ERR_LOGIN = (By.CLASS_NAME, 'login_form_error')
