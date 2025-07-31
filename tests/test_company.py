import pytest, json
from pages.company_master_page import CompanyMasterPage

with open("utilities/test_data/company_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("data",test_data)

def test_company_master(driver,data):
    page = CompanyMasterPage(driver)
    page.login(data["email"], data["password"])
    page.navigate_to_company_master()
    page.add_company(data)
