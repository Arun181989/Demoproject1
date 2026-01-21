from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    HOME_URL = "https://ekalya.in/"
    PAGE_TITLE = "ekayla"

    CONTACT_MENU = (By.XPATH, "//a[contains(text(),'Contact')]")
    HEADER = (By.TAG_NAME, "header")
    MENU_ITEM = lambda self, name: (By.LINK_TEXT, name)

    def open(self):
        self.driver.get(self.HOME_URL)

    def is_home_page_loaded(self):
        return self.PAGE_TITLE in self.get_title().lower()

    def is_banner_visible(self):
        return self.wait.until(
            lambda d: d.find_element(*self.HEADER).is_displayed()
        )

    def go_to_contact_page(self):
        self.click(self.CONTACT_MENU)

    def click_menu(self, menu_name):
        self.click(self.MENU_ITEM(menu_name))
