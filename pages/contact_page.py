from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ContactPageLocators



class ContactPage(BasePage):

    NAME = (By.XPATH, "//input[contains(@placeholder,'Name')]")
    EMAIL = (By.XPATH, "//input[contains(@placeholder,'Email')]")
    MESSAGE = (By.XPATH, "//textarea")
    SUBMIT = (By.XPATH, "//button[contains(text(),'Send') or contains(text(),'Submit')]")

    def submit_form(self, name, email, message):
        self.type(ContactPageLocators.NAME_INPUT, name)
        self.type(ContactPageLocators.EMAIL_INPUT, email)
        self.type(ContactPageLocators.MESSAGE_TEXTAREA, message)
        self.click(ContactPageLocators.SUBMIT_BUTTON)
