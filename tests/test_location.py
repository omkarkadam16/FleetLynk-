import pytest, json
from pages.location_master_page import LocationMasterPage

with open("utilities/test_data/location_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("data",test_data)

def test_location_master(driver,data):
    page = LocationMasterPage(driver)
    page.login(data["email"],data["password"])
    page.navigate_to_location_master()
    page.add_location(data)