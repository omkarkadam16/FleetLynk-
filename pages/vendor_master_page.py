from utilities.helpers import *

class VendorMasterPage:

    def __init__(self,driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.get("https://win-8tcj8ivog5i:7265/")
        send_keys(self.driver, By.ID, "EmailId", email)
        send_keys(self.driver, By.ID, "Password", password)
        click_element(self.driver, By.ID, "loginButton")

    def navigate_vendor_master(self):
        click_element(self.driver, By.LINK_TEXT, "Master")
        click_element(self.driver, By.LINK_TEXT, "Vendor")

    def add_vendor(self,data):
        switch_frames(self.driver, "addVendor")
        click_element(self.driver, By.ID, "addVendor")
        switch_frames(self.driver, "txtGstNumber")
        send_keys(self.driver, By.ID, "txtGstNumber", data["gst"])
        click_element(self.driver, By.ID, "gstEKycButton")
        send_keys(self.driver, By.ID, "txtPanNumber", data["pan"])
        click_element(self.driver, By.ID, "panEKycButton")
        send_keys(self.driver, By.ID, "txtVendorName", data["vendor"])
        time.sleep(2)
        select_dropdown(self.driver,By.ID,"select2-ddlVendorCategory-container",data["category"])
        send_keys(self.driver, By.ID, "txtAddress", data["address"])
        time.sleep(2)
        select_dropdown(self.driver, By.ID, "select2-ddlCity-container", data["city"])
        send_keys(self.driver, By.ID, "txtEmailId", data["email_id"])
        send_keys(self.driver, By.ID, "txtContactPerson", data["contact_person"])
        send_keys(self.driver, By.ID, "txtPinCode", data["pincode"])
        send_keys(self.driver, By.ID, "txtWhatsappNumber", data["whatsapp_number"])
        send_keys(self.driver, By.ID, "txtMobileNumber", data["mobile_number"])
        click_element(self.driver, By.ID, "btnSaveVendor")
        time.sleep(2)