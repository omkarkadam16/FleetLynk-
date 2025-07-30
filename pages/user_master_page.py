from utilities.helpers import *

class UserMasterPage():
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        send_keys(self.driver,By.ID, "EmailId", email)
        send_keys(self.driver, By.ID, "Password", password)
        click_element(self.driver, By.ID, "loginButton")

    def navigate_to_user_master(self):
        click_element(self.driver, By.LINK_TEXT, "Company")
        click_element(self.driver, By.LINK_TEXT, "User")

    def add_user(self, data):
        switch_frames(self.driver, "btnAddUser")
        click_element(self.driver, By.ID, "btnAddUser")
        switch_frames(self.driver, "userbodyform")

        print("Typing Name")
        send_keys(self.driver, By.ID, "txtName", data["name"])
        print("Typing Login Name")
        send_keys(self.driver, By.ID, "txtLoginName", data["login_name"])
        send_keys(self.driver, By.ID, "txtPassword", data["password"])
        send_keys(self.driver, By.ID, "txtEmailid", data["email"])
        select_dropdown(self.driver, By.ID, "select2-ddlCompanyAndFranchise-container", data["company"])
        select_dropdown(self.driver, By.ID, "select2-ddlLocation-container", data["location"])
        send_keys(self.driver, By.ID, "txtMobileNo", data["mobile"])
        click_element(self.driver, By.ID, "btnSaveForm")
        time.sleep(4)