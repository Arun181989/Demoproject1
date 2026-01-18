import pytest

from pages.home_page import HomePage
from pages.contact_page import ContactPage


@pytest.mark.regression
def test_contact_form_submission(driver):
    home = HomePage(driver)
    home.go_to_contact_page()

    contact = ContactPage(driver)
    contact.submit_form(
        name="Test User",
        email="testuser@example.com",
        message="This is an automation test inquiry"
    )

    assert "contact" in driver.current_url.lower()
