from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import step
from pages.textbox_page import TextBoxPage

@step("el usuario está en la página de DemoQA")
def user_on_demoqa_page(context):
    context.demoqa_page = TextBoxPage(context.driver)

@step('clicamos sobre el apartado "{menu}"')
def click_elements_section(context, menu):
    wait = WebDriverWait(context.driver, 1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//h5[text()='{menu}']")))
    element.click()

@step('nos dirigimos a "{option}"')
def navigate_to_text_box(context, option):
    wait = WebDriverWait(context.driver, 1)

    option_map = {
        "text box": "item-0",
        "check box": "item-1",
        "radio button": "item-2",
        "web tables": "item-3",
        "buttons": "item-4",
        "links": "item-5",
        "broken links - images": "item-6",
        "upload and download": "item-7",
        "dynamic properties": "item-8",
    }

    option_id = option_map.get(option.lower())
    if option_id is None:
        raise AssertionError(f"Opción no válida: {option}")

    element = wait.until(EC.element_to_be_clickable((By.ID, option_id)))
    element.click()