import pytest
import json
from pages.franchise_master_page import FranchiseMasterPage

# Load data as list
with open("utilities/test_data/franchise_data.json") as f:
    test_data = json.load(f)  # Load JSON test data

# Parametrize test using the loaded data
@pytest.mark.parametrize("data", test_data)
def test_create_franchise(driver, data):
    page = FranchiseMasterPage(driver)
    page.login(data["email"], data["password"])
    page.navigate_to_master()
    page.add_franchise(data)