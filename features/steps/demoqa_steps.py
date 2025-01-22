import time
from selenium.webdriver.common.by import By
from behave import step
from pages.demoqa_page import DemoQAPage

@step("el usuario está en la página de DemoQA")
def user_on_demoqa_page(context):
    context.demoqa_page = DemoQAPage(context.driver)
    context.demoqa_page.load()

@step("clicamos sobre el apartado \"Elements\"")
def click_elements_section(context):
    context.demoqa_page.click_elements()

@step("nos dirigimos a \"Text Box\"")
def navigate_to_text_box(context):
    context.demoqa_page.click_text_box()

@step("interactúa con el formulario de registro")
def user_interacts_with_form(context):
    for row in context.table:
        first_name = row["first_name"]
        last_name = row["last_name"]
        context.demoqa_page.fill_text_box(first_name, last_name)
        time.sleep(3)  # Espera para que se procese la acción

@step("el formulario es enviado correctamente")
def form_is_submitted(context):
    success_message = context.driver.find_element(By.ID, "submit-message")
    assert success_message.is_displayed(), "El formulario no se envió correctamente"
