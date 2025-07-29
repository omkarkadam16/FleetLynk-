import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium.common.exceptions as ex
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    # Setup code (equivalent to setUpClass)
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--start-maximized')
    options.add_argument('--incognito')

    # Disable password manager & credential services
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
    }
    options.add_experimental_option("prefs", prefs)

    # Launch Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 10)

    yield driver  # Yielding the driver to the test functions

    # Teardown code (equivalent to tearDownClass)
    driver.quit()


def click_element(driver, by, value, retry=2):
    for i in range(retry):
        try:
            driver.wait.until(EC.element_to_be_clickable((by, value))).click()
            print("Clicked on element", value)
            return True
        except (ex.ElementClickInterceptedException,
                ex.StaleElementReferenceException,
                ex.TimeoutException):
            print(f"Retrying click on {by} with value {value}, attempt {i+1}/{retry}")
            time.sleep(1)
    try:
        element = driver.find_element(by, value)
        driver.execute_script("arguments[0].click();", element)
        print("Clicked on element using JavaScript")
        return True
    except ex.JavascriptException:
        return False


def switch_frames(driver, element_id):
    driver.switch_to.default_content()
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        try:
            if driver.find_element(By.ID, element_id):
                return True
        except ex.NoSuchElementException:
            driver.switch_to.default_content()
    return False


def send_keys(driver, by, value, text):
    try:
        element = driver.wait.until(EC.visibility_of_element_located((by, value)))
        element.is_enabled()
        element.clear()
        element.send_keys(text)
        print("Sent keys", text)
        return True
    except ex.NoSuchElementException:
        print(f"Element not found: {value}")
        return False


def select_dropdown(driver, by, value, text):
    try:
        # Click the dropdown to activate the input (if necessary)
        click_element(driver, by, value)
        # Send input text (Search field Class Name)
        input_box = driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field")))
        input_box.clear()
        input_box.send_keys(text)
        print(f"Typed '{text}' in autocomplete input")
        # Wait for the results to appear (List Class name)
        driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select2-selection__rendered")))
        # Get all matching options
        options = driver.find_elements(By.CLASS_NAME, "select2-selection__rendered")
        for option in options:
            if text.lower() in option.text.strip().lower():
                option.click()
                print("Selected autocomplete option:", option.text.strip())
                return True
        # Fallback: select first with keyboard
        input_box.send_keys(Keys.DOWN)
        input_box.send_keys(Keys.ENTER)
        print("Fallback: selected autocomplete option with keyboard")
        return True
    except Exception as e:
        print(f"[ERROR] Autocomplete selection failed for '{text}':", e)
        return False


def handle_alert(driver, accept=True, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        return True
    except ex.NoAlertPresentException:
        print("[INFO] No alert to handle.")
        return False


# Example Test Case
def test_service_network(driver):
    driver.get("https://win-8tcj8ivog5i:7265/")
    print("Logging in...")
    send_keys(driver, By.ID, "EmailId", "demo123@gmail.com")
    send_keys(driver, By.ID, "Password", "Demo@123")
    click_element(driver, By.ID, "loginButton")
    print("Login successful.")

    time.sleep(2)
    click_element(driver, By.LINK_TEXT, "Master")
    click_element(driver, By.LINK_TEXT, "Profile Rights")

    switch_frames(driver, "ProFileBodyForm")
    switch_frames(driver, "select2-txtName-container")
    select_dropdown(driver, By.ID, "select2-txtName-container", "Admin")
    time.sleep(2)
    select_dropdown(driver, By.ID, "select2-txtMenu-container", "Master")

    click_element(driver, By.ID, "add1")
    time.sleep(1)

    click_element(driver, By.ID, "btnSaveForm")
    time.sleep(2)

