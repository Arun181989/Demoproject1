from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import FooterLocators

class FooterPage(BasePage):

    def scroll_to_footer(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def is_footer_visible(self):
        self.scroll_to_footer()
        return self.is_visible(FooterLocators.COPYRIGHT_TEXT)
