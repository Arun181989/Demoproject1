import pytest

from pages.home_page import HomePage

@pytest.mark.smoke
def test_home_page_loads(driver):
    home = HomePage(driver)
    home.open()
    assert home.is_home_page_loaded()
    assert home.is_banner_visible()

