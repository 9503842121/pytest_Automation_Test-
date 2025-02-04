
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class AutomationFormPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys(phone)

    def select_gender(self, gender):
        gender_radio = self.driver.find_element(By.XPATH, "//label[normalize-space()='Male']")
        gender_radio.click()

    def enter_address(self, address):
        self.driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(address)

    def select_state(self, state):
        state_dropdown = self.driver.find_element(By.ID, "state")
        state_dropdown.click()
        self.driver.find_element(By.XPATH, "//div[@id='react-select-3-option-0']").click()

    def select_city(self, city):
        city_dropdown = self.driver.find_element(By.ID, "city")
        city_dropdown.click()
        self.driver.find_element(By.XPATH, "//div[@id='react-select-4-option-0']").click()

    def submit_form(self):
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text

    def select_hobby(self, param):
        pass

    def enter_subject(self, param):
        pass

    def enter_date_of_birth(self, param):
        pass
