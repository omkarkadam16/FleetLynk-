from selenium.webdriver.common.by import By
from utilities.helpers import *

class ProfileRightsPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        send_keys(self.driver, By.ID, "EmailId", email)
        send_keys(self.driver, By.ID, "Password", password)
        click_element(self.driver, By.ID, "loginButton")

    def navigate_to_profile_rights(self):
        click_element(self.driver, By.LINK_TEXT, "Master")
        click_element(self.driver, By.LINK_TEXT, "Profile Rights")

    def add_profile_right(self, profile_name, menu_name):
        switch_frames(self.driver, "ProFileBodyForm")
        switch_frames(self.driver, "select2-txtName-container")
        select_dropdown(self.driver, By.ID, "select2-txtName-container", profile_name)
        select_dropdown(self.driver, By.ID, "select2-txtMenu-container", menu_name)
        click_element(self.driver, By.ID, "add1")
        click_element(self.driver, By.ID, "btnSaveForm")
