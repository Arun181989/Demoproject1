"""
TC_ID: TC_FOOTER_01
CRS_ID: CRS_05
Verify footer is visible on all pages
"""
from pages.footer_page import FooterPage
from pages.home_page import HomePage

def test_TC_FOOTER_01(driver):
    home = HomePage(driver)
    home.open()   # 👈 IMPORTANT

    footer = FooterPage(driver)
    assert footer.is_footer_visible()
