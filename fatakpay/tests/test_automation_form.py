
import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.driver_setup import get_driver
from pages.automation_form_page import AutomationFormPage
from selenium .webdriver.support.select import Select

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    driver.get("https://demoqa.com/automation-practice-form")
    yield driver
    # driver.quit()

def test_page_title(driver):
    assert driver.title == "DEMOQA"

def test_first_name_field(driver):
    form_page = AutomationFormPage(driver)
    form_page.enter_first_name("Rahul")
    assert driver.find_element(By.ID, "firstName").get_attribute("value") == "Rahul"


def test_invalid_email(driver):
    form_page = AutomationFormPage(driver)
    form_page.enter_email("Rahulthakare@gmail")

def test_gender_selection(driver):
    form_page = AutomationFormPage(driver)
    form_page.select_gender('Male')
    male_radio_button = driver.find_element(By.XPATH, "//input[@name='gender'][@value='Male']")
    assert male_radio_button.is_selected(), "Male gender radio button is not selected"

def test_phone_field(driver):
    form_page = AutomationFormPage(driver)
    form_page.enter_phone("1234567890")
    assert driver.find_element(By.ID, "userNumber").get_attribute("value") == "1234567890"


def test_address_field(driver):
    form_page = AutomationFormPage(driver)
    form_page.enter_address("123 Main St")
    assert driver.find_element(By.ID, "currentAddress").get_attribute("value") == "123 Main St"

def test_state_and_city_selection(driver):
    form_page = AutomationFormPage(driver)
    form_page.select_state("NCR")
    form_page.select_city("Delhi")
    selected_state = driver.find_element(By.ID, "state").get_attribute("value")
    selected_city = driver.find_element(By.ID, "city").get_attribute("value")


def test_form_submission(driver):
    form_page = AutomationFormPage(driver)

    form_page.enter_first_name("Rahul")
    form_page.enter_last_name("Thakare")
    form_page.enter_email("Rahulthakare@gmail.com")
    form_page.enter_phone("1234567890")
    form_page.enter_address("123 Main St")
    form_page.select_gender("Male")

    state_dropdown = driver.find_element(By.ID, "state")
    driver.execute_script("arguments[0].scrollIntoView();", state_dropdown)


    try:
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        driver.switch_to.default_content()
    except:
        pass


    driver.execute_script("arguments[0].click();", state_dropdown)
    form_page.select_state("NCR")
    form_page.select_city("Delhi")
    form_page.submit_form()


    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='modal-title h4']"))
    ).text

    print("Success Message:", success_message)
    assert "Thanks for submitting the form" in success_message, "❌ Form submission failed!"

