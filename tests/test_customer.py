import pytest,json
from pages.customer_master_page import CustomerMasterPage

with open("utilities/test_data/customer_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("data",test_data)

def test_customer(driver,data):

    page = CustomerMasterPage(driver)
    page.login(data["email"], data["password"])
    page.navigate_customer_master()
    page.add_customer(data)