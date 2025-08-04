from utilities.helpers import *

class CustomerMasterPage:

    def __init__(self,driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.get("https://win-8tcj8ivog5i:7265/")
        send_keys(self.driver, By.ID, "EmailId", email)
        send_keys(self.driver, By.ID, "Password", password)
        click_element(self.driver, By.ID, "loginButton")

    def navigate_customer_master(self):
        click_element(self.driver, By.LINK_TEXT, "Master")
        click_element(self.driver, By.LINK_TEXT, "Customer")

    def add_customer(self,data):
        switch_frames(self.driver, "btnAddCustomer")
        click_element(self.driver, By.ID, "btnAddCustomer")
        switch_frames(self.driver, "txtGstNumber")
        send_keys(self.driver, By.ID, "txtGstNumber", data["gst"])
        click_element(self.driver, By.ID, "gstEKycButton")
        send_keys(self.driver, By.ID, "txtPanNumber", data["pan"])
        click_element(self.driver, By.ID, "panEKycButton")
        send_keys(self.driver, By.ID, "txtCustomerName", data["customer"])
        send_keys(self.driver, By.ID, "txtEmail", data["email_id"])
        send_keys(self.driver, By.ID, "txtaddress", data["address"])
        select_dropdown(self.driver, By.ID, "select2-ddlCity-container", data["city"])
        send_keys(self.driver, By.ID, "txtContactPerson", data["contact_person"])
        send_keys(self.driver, By.ID, "numPincode", data["pincode"])
        send_keys(self.driver, By.ID, "numContact", data["contact_number"])
        send_keys(self.driver, By.ID, "numWhatsApp", data["whatsapp_number"])
        send_keys(self.driver, By.ID, "numMobile", data["mobile_number"])
        click_element(self.driver, By.ID, "btnSaveCustomer")
        time.sleep(2)

