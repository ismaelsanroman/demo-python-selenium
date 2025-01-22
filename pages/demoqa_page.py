from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DemoQAPage:
    def __init__(self, driver):
        self.driver = driver
        self.elements_section = (By.XPATH, "//h5[text()='Elements']")
        self.text_box_option = (By.ID, "item-0")
        self.first_name = (By.ID, "userName")
        self.last_name = (By.ID, "userEmail")
        self.submit_button = (By.ID, "submit")

    def load(self):
        self.driver.get("https://demoqa.com")

    def click_elements(self):
        self.driver.find_element(*self.elements_section).click()

    def click_text_box(self):
        self.driver.find_element(*self.text_box_option).click()

    def fill_text_box(self, first_name, last_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.submit_button).click()
