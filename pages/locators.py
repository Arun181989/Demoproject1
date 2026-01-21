from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGO = (By.XPATH, "//a[contains(@class,'logo')]")
    COURSES_MENU = (By.LINK_TEXT, "Courses")
    CONTACT_MENU = (By.LINK_TEXT, "Contact")


class CoursesPageLocators:
    COURSE_CARDS = (By.CSS_SELECTOR, "div.course")
    COURSE_TITLES = (By.CSS_SELECTOR, ".course-card h3")


class ContactPageLocators:
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    MESSAGE_TEXTAREA = (By.NAME, "message")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")


class FooterLocators:
    COPYRIGHT_TEXT = (By.XPATH, "//*[contains(text(),'©')]")
    PRIVACY_LINK = (By.LINK_TEXT, "Privacy Policy")
    TERMS_LINK = (By.LINK_TEXT, "Terms")
    CONTACT_LINK = (By.LINK_TEXT, "Contact")