from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CoursesPage(BasePage):

    # Broad but reliable locator
    COURSE_ITEMS = (By.XPATH, "//a[contains(@href,'course') or contains(@href,'program')]")

    def is_courses_page_loaded(self):
        return "course" in self.driver.current_url.lower()

    def get_course_names(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.COURSE_ITEMS)
        )

        names = []
        for el in elements:
            text = el.text.strip()
            if text:
                names.append(text)

        return names

    def get_course_count(self):
        return len(self.get_course_names())
