import pytest
import json
from pages.user_master_page import UserMasterPage

# Load data as list
with open("utilities/test_data/user_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("data", test_data)
def test_create_user(driver, data):
    driver.get("https://win-8tcj8ivog5i:7265/")
    page = UserMasterPage(driver)
    page.login(data["username"], data["password"])
    page.navigate_to_user_master()
    page.add_user(data)
