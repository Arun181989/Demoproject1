import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage


@pytest.mark.xfail(reason="Contact form backend not implemented")
def test_contact_form_submission(driver):
    home = HomePage(driver)
    home.go_to_contact_page()

    contact = ContactPage(driver)
    contact.submit_form("Test User", "test@example.com", "Test Message")
