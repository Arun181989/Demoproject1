import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from utils.data_reader import read_csv

test_data = read_csv("data/contact_data.csv")

import pytest

@pytest.mark.xfail(reason="Contact form redirects to 404 due to missing backend")
@pytest.mark.parametrize("data", test_data)
def test_contact_form_with_csv(driver, data):
    home = HomePage(driver)
    home.go_to_contact_page()

    contact = ContactPage(driver)
    contact.submit_form(
        name=data["name"],
        email=data["email"],
        message=data["message"]
    )

    assert "this page does not exist" not in driver.page_source.lower()



