from utilities.helpers import *

class FranchiseMasterPage:
    def __init__(self,driver):
        self.driver = driver

    def login(self,email,password):
        self.driver.get("https://win-8tcj8ivog5i:7265/")
        send_keys(self.driver,By.ID,"EmailId",email)
        send_keys(self.driver,By.ID,"Password",password)
        click_element(self.driver,By.ID,"loginButton")

    def navigate_to_master(self):
        click_element(self.driver,By.LINK_TEXT,"Master")
        click_element(self.driver,By.LINK_TEXT,"Franchise")

    def add_franchise(self,data):
        switch_frames(self.driver,"btnAddFranchise")
        click_element(self.driver,By.ID,"btnAddFranchise")
        switch_frames(self.driver,"txtFranchiseName")
        send_keys(self.driver,By.ID,"txtFranchiseName",data["franchise_name"])
        upload_file_in_dropzone(self.driver,"C:\\Users\\Admin\\Pictures\\4k-ducati-wallpaper.jpg")
        select_dropdown(self.driver,By.ID,"select2-ddlCity-container",data["city"])
        send_keys(self.driver,By.ID,"txtAddress",data["address"])
        send_keys(self.driver,By.ID,"txtContactPerson",data["contact_person"])
        send_keys(self.driver,By.ID,"txtPinCode",data["pincode"])
        send_keys(self.driver,By.ID,"txtContactNumber",data["contact_number"])
        send_keys(self.driver,By.ID,"txtWhatsAppNumber",data["whatsapp_number"])
        send_keys(self.driver,By.ID,"txtMobileNumber",data["mobile_number"])
        send_keys(self.driver,By.ID,"txtEmailId",data["email_id"])
        send_keys(self.driver,By.ID,"txtPanNumber",data["pan_number"])
        send_keys(self.driver,By.ID,"txtGstNumber",data["gst_number"])
        click_element(self.driver,By.ID,"btnSaveFranchise")
        time.sleep(2)

