from utilities.helpers import *

class LocationMasterPage:

    def __init__(self,driver):
        self.driver = driver

    def login(self,email,password):
        self.driver.get("https://win-8tcj8ivog5i:7265/")
        send_keys(self.driver, By.ID, "EmailId", email)
        send_keys(self.driver, By.ID, "Password", password)
        click_element(self.driver, By.ID, "loginButton")

    def navigate_to_location_master(self):
        click_element(self.driver, By.LINK_TEXT, "Master")
        click_element(self.driver, By.LINK_TEXT, "Location")

    def add_location(self,data):
        switch_frames(self.driver, "btnAddLocation")
        click_element(self.driver, By.ID, "btnAddLocation")
        switch_frames(self.driver, "txtLocationName")

        send_keys(self.driver,By.ID,"txtLocationName",data["location"])
        send_keys(self.driver,By.ID,"txtPerson",data["person"])
        send_keys(self.driver,By.ID,"txtAddress",data["address"])
        select_dropdown(self.driver,By.ID,"select2-ddlCity-container",data["city"])
        send_keys(self.driver, By.ID, "txtContactNumber", data["contact"])
        send_keys(self.driver, By.ID, "txtWhatsAppNumber", data["whatsapp"])
        send_keys(self.driver, By.ID, "txtMobileNumber", data["mobile"])
        send_keys(self.driver, By.ID, "txtEmail", data["email_id"])
        send_keys(self.driver, By.ID, "txtPinCode", data["pincode"])

        click_element(self.driver,By.ID,"btnSaveForm")
        time.sleep(2)



