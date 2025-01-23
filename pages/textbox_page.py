from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.text_box_option = (By.ID, "item-0")
        self.full_name = (By.ID, "userName")
        self.email = (By.ID, "userEmail")
        self.current_address = (By.ID, "currentAddress")
        self.permanent_address = (By.ID, "permanentAddress")
        self.submit_button = (By.XPATH, '//*[@id="submit"]')
        
        # Path para verificar los datos
        self.verify_full_name = (By.XPATH, "//p[@id='name']")
        self.verify_email = (By.XPATH, "//p[@id='email']")
        self.verify_current_address = (By.XPATH, "//p[@id='currentAddress']")
        self.verify_permanent_address = (By.XPATH, "//p[@id='permanentAddress']")

    def click_elements(self, path):
        """Hace clic en un elemento"""
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.element_to_be_clickable(path))
        element.click()

    def fill_text_box(self, full_name, email, current_address, permanent_address):
        """Rellena el formulario de TextBox"""
        self.driver.find_element(*self.full_name).send_keys(full_name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.current_address).send_keys(current_address)
        self.driver.find_element(*self.permanent_address).send_keys(permanent_address)

    def get_verification_text(self, field):
        """Obtiene el texto mostrado después de enviar el formulario."""
        field_mapping = {
            "full_name": self.verify_full_name,
            "email": self.verify_email,
            "current_address": self.verify_current_address,
            "permanent_address": self.verify_permanent_address
        }

        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located(field_mapping[field]))
        return element.text  # ✅ Solo devuelve el texto, sin validaciones

    def validate_form_submission(self, expected_values):
        """Valida que los valores ingresados coincidan con los valores mostrados en la página."""
        expected_full_name = f"Name:{expected_values['full_name']}"
        expected_email = f"Email:{expected_values['email']}"
        expected_current_address = f"Current Address :{expected_values['current_address']}"
        expected_permanent_address = f"Permananet Address :{expected_values['permanent_address']}"

        actual_full_name = self.get_verification_text("full_name")
        actual_email = self.get_verification_text("email")
        actual_current_address = self.get_verification_text("current_address")
        actual_permanent_address = self.get_verification_text("permanent_address")

        assert expected_full_name == actual_full_name, f"Error: El nombre no coincide. Esperado: '{expected_full_name}', Actual: '{actual_full_name}'"
        assert expected_email == actual_email, f"Error: El email no coincide. Esperado: '{expected_email}', Actual: '{actual_email}'"
        assert expected_current_address == actual_current_address, f"Error: La dirección actual no coincide. Esperado: '{expected_current_address}', Actual: '{actual_current_address}'"
        assert expected_permanent_address == actual_permanent_address, f"Error: La dirección permanente no coincide. Esperado: '{expected_permanent_address}', Actual: '{actual_permanent_address}'"
