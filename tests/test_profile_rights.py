import pytest
import json
from pages.profile_rights_page import ProfileRightsPage

# Load JSON test data
with open('utilities/test_data/profile_rights_data.json') as f:
    test_data = json.load(f)

@pytest.mark.parametrize("data", test_data)
def test_add_profile_right(driver, data):
    driver.get("https://win-8tcj8ivog5i:7265/")  # Or your live test URL

    page = ProfileRightsPage(driver)
    page.login(data["email"], data["password"])
    page.navigate_to_profile_rights()
    page.add_profile_right(data)

    # Basic check (customize this for your actual success message or alert)
    assert "Profile" in driver.page_source
