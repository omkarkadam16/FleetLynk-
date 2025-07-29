from pages.profile_rights_page import ProfileRightsPage
from utilities.webdriver_setup import driver

def test_add_profile_right(driver):
    driver.get("https://win-8tcj8ivog5i:7265/")

    profile_page = ProfileRightsPage(driver)
    profile_page.login("demo123@gmail.com", "Demo@123")
    profile_page.navigate_to_profile_rights()
    profile_page.add_profile_right("Admin", "Master")

    assert "Profile" in driver.page_source
