from utilities.helpers import *

class CompanyMasterPage:

    def __init__(self,driver):
        self.driver = driver

    def login(self,email,password):
        self.driver.get("https://win-8tcj8ivog5i:7265/")
        send_keys(self.driver,By.ID,"EmailId",email)
        send_keys(self.driver,By.ID,"Password",password)
        click_element(self.driver,By.ID,"loginButton")

    def navigate_to_company_master(self):
        click_element(self.driver,By.LINK_TEXT,"Company")
        click_element(self.driver,By.LINK_TEXT,"Corporate Company")

    def add_company(self,data):
        switch_frames(self.driver,"addCompany")
        click_element(self.driver,By.ID,"addCompany")
        switch_frames(self.driver,"txtCompanyName")

        send_keys(self.driver,By.ID,"txtCompanyName",data["company_name"])
        select_dropdown(self.driver,By.ID,"select2-ddlFranchisename-container",data["franchise_name"])
        send_keys(self.driver,By.ID,"txtAddress",data["address"])
        select_dropdown(self.driver,By.ID,"select2-ddlCity-container",data["city"])
        send_keys(self.driver,By.ID,"txtPinCode",data["pincode"])
        send_keys(self.driver,By.ID,"txtPerson",data["contact_person"])
        send_keys(self.driver,By.ID,"txtContactNumber",data["contact_number"])
        send_keys(self.driver,By.ID,"txtWhatsAppNumber",data["whatsapp_number"])
        send_keys(self.driver,By.ID,"txtMobileNumber",data["mobile_number"])
        send_keys(self.driver,By.ID,"txtEmail",data["email_id"])
        send_keys(self.driver,By.ID,"txtPanNumber",data["pan_number"])
        send_keys(self.driver,By.ID,"txtGstNumber",data["gst_number"])
        click_element(self.driver,By.ID,"btnSaveCompanyType")
        time.sleep(2)
