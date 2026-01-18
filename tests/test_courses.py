from pages.home_page import HomePage
from pages.courses_page import CoursesPage

def test_courses_list_displayed(driver):
    home = HomePage(driver)
    home.click_menu("Courses")

    courses = CoursesPage(driver)

    course_names = courses.get_course_names()

    assert len(course_names) > 0, "No courses were displayed"

    for course in course_names:
        assert course.strip() != ""
