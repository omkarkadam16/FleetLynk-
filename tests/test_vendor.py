import pytest, json
from pages.vendor_master_page import VendorMasterPage

with open("utilities/test_data/vendor_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("data",test_data)

def test_vendor(driver,data):
    page = VendorMasterPage(driver)
    page.login(data["email"], data["password"])
    page.navigate_vendor_master()
    page.add_vendor(data)

