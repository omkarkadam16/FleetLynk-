import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as ex
from selenium.webdriver.support.ui import WebDriverWait

def click_element(driver, by, value, retry=2):
    for i in range(retry):
        try:
            driver.wait.until(EC.element_to_be_clickable((by, value))).click()
            print("Clicked:", value)
            return True
        except (ex.ElementClickInterceptedException, ex.StaleElementReferenceException, ex.TimeoutException):
            time.sleep(1)
    try:
        element = driver.find_element(by, value)
        driver.execute_script("arguments[0].click();", element)
        print("Clicked using JS:", value)
        return True
    except ex.JavascriptException:
        return False

def send_keys(driver, by, value, text):
    try:
        click_element(driver, by, value)
        element = driver.wait.until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)
        return True
    except(ex.ElementClickInterceptedException,
                ex.StaleElementReferenceException,
                ex.TimeoutException):
        return False

def switch_frames(driver, element_id):
    driver.switch_to.default_content()
    for iframe in driver.find_elements(By.TAG_NAME, "iframe"):
        driver.switch_to.frame(iframe)
        try:
            if driver.find_element(By.ID, element_id):
                return True
        except ex.TimeoutException:
            driver.switch_to.default_content()
    return False

def select_dropdown(driver, by, value, text):
    try:
        click_element(driver, by, value)
        time.sleep(1)
        input_box = driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field")))
        input_box.clear()
        input_box.send_keys(text)
        print("Entered:", text)
        input_box.send_keys(Keys.ENTER)
        return True
    except(ex.ElementClickInterceptedException,
                ex.StaleElementReferenceException,
                ex.TimeoutException):
        return False

def handle_alert(driver, accept=True, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Alert:", alert.text)
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        return True
    except ex.NoAlertPresentException:
        return False

def upload_file_in_dropzone(self, file_path):
    try:
        # Wait for the Dropzone input to appear
        file_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.dz-hidden-input"))
        )
        # Send file path to hidden file input
        file_input.send_keys(file_path)
        print("✅ File uploaded successfully:", file_path)
        return True
    except Exception as e:
        print("Upload failed:", e)
        return False

