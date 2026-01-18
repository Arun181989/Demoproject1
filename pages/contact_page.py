from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):

    NAME = (By.XPATH, "//input[contains(@placeholder,'Name')]")
    EMAIL = (By.XPATH, "//input[contains(@placeholder,'Email')]")
    MESSAGE = (By.XPATH, "//textarea")
    SUBMIT = (By.XPATH, "//button[contains(text(),'Send') or contains(text(),'Submit')]")

    def submit_form(self, name, email, message):
        self.enter_text(self.NAME, name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.MESSAGE, message)
        self.click(self.SUBMIT)
