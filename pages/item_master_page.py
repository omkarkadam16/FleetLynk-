from utilities.helpers import *

class ItemMasterPage:

    def __init__(self,driver):
        self.driver = driver

    def login(self,email,password):
        self.driver.get("https://win-8tcj8ivog5i:7265/")
        send_keys(self.driver,By.ID,"EmailId",email)
        send_keys(self.driver,By.ID,"Password",password)
        click_element(self.driver,By.ID,"loginButton")

    def navigate_item_master(self):
        click_element(self.driver,By.LINK_TEXT,"Master")
        click_element(self.driver, By.LINK_TEXT, "Item Or Product")

    def add_item(self,data):
        switch_frames(self.driver,"btnAddProduct")
        click_element(self.driver,By.ID,"btnAddProduct")

        send_keys(self.driver,By.ID,"txtItemName",data["item"])

        click_element(self.driver,By.ID,"btnSaveProduct")

