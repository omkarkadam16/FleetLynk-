import pytest,json
from pages.item_master_page import ItemMasterPage

with open("utilities/test_data/item_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("data",test_data)

def test_item(driver,data):
    page = ItemMasterPage(driver)

    page.login(data["email"],data["password"])
    page.navigate_item_master()
    page.add_item(data)