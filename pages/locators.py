from selenium.webdriver.common.by import By

class PageLocators:
    NAME_F = (By.ID, "name-input")
    PASSWORD_F = (By.XPATH, '//input[@type="password"]')
    MILK_F = (By.ID, "drink2")
    COFFEE_F = (By.ID, "drink3")
    CHECKBOX_YELLOW = (By.ID, "color3")
    SELECTOR = (By.ID, "automation")
    SELECTOR_VALUE = (By.XPATH, "//option[@value='yes']")
    AUTOMATION_LIST = (By.CSS_SELECTOR, "#feedbackForm > ul > li")
    EMAIL_F = (By.ID, "email")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submit-btn")