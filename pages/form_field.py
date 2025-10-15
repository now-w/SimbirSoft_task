from .base_page import BasePage
from .locators import PageLocators
from selenium.common.exceptions import NoAlertPresentException
import time
import allure

class FormField(BasePage):

    def fill_name(self, name):
        self.driver.find_element(*PageLocators.NAME_F).send_keys(name)
        self.scroll_to_element(PageLocators.NAME_F)
        time.sleep(1)

    def fill_password(self, password):
        self.driver.find_element(*PageLocators.PASSWORD_F).send_keys(password)

    def choose_milk(self):
        self.driver.find_element(*PageLocators.MILK_F).click()

    def choose_coffee(self):
        self.driver.find_element(*PageLocators.COFFEE_F).click()
        self.scroll_to_element(PageLocators.COFFEE_F)

    def choose_yellow(self):
        time.sleep(1)
        self.driver.find_element(*PageLocators.CHECKBOX_YELLOW).click()

    def automation_yes(self):
        selector = self.driver.find_element(*PageLocators.SELECTOR)
        time.sleep(1)
        selector.click()
        self.driver.find_element(*PageLocators.SELECTOR_VALUE).click()

    def count_auto_tools(self):
        tools = self.driver.find_elements(*PageLocators.AUTOMATION_LIST)
        amount = len(tools)
        return amount

    def max_symbols(self):
        time.sleep(1)

        auto_tools_list = self.driver.find_elements(*PageLocators.AUTOMATION_LIST)

        longest_tool = ""

        for tool in auto_tools_list:
            if len(tool.text) > len(longest_tool):
                longest_tool = tool.text

        return longest_tool

    def fill_email(self, email):
        self.driver.find_element(*PageLocators.EMAIL_F).send_keys(email)
        self.scroll_to_element(PageLocators.EMAIL_F)

    def fill_message(self):
        message = self.driver.find_element(*PageLocators.MESSAGE)
        time.sleep(1)
        message.send_keys(f"{self.count_auto_tools()} '_' {self.max_symbols()}")

    def submit(self):
        self.driver.find_element(*PageLocators.SUBMIT).click()

    @allure.step("Алерт отобразился")
    def submit_result(self):
        alert = self.driver.switch_to.alert
        assert alert.text == "Message received!"
        alert.accept()

    @allure.step("Алерт не отобразился")
    def no_submit_alert(self):
        try:
            alert = self.driver.switch_to.alert
            allure.attach(f"Обнаружен алерт: '{alert.text}'", attachment_type=allure.attachment_type.TEXT)
            alert.accept()
            raise AssertionError("Обнаружен алерт.")
        except NoAlertPresentException:
            return True