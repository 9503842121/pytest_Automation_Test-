
import time
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller. install()


def get_driver():
    driver=webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(5)
    return driver
