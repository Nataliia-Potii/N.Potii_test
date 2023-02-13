from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"C:\Users\NP\N.Potii_QA_Auto"
    DRIVER_NAME = "chromedriver"

    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
            )

    def close(self):
        self.driver.close()
