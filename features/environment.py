from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.textbox_page import TextBoxPage  # ✅ Importamos la clase necesaria

def before_all(context):
    """Se ejecuta antes de todas las pruebas, inicializa el WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Opcional, quitar si quieres ver la ejecución
    options.add_argument("--start-maximized")  # Maximizar ventana para evitar problemas
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

def before_scenario(context, scenario):
    """Se ejecuta antes de cada escenario"""
    context.driver.get("https://demoqa.com")

    # ✅ Se inicializa TextBox_Page aquí para que esté disponible en los steps
    context.TextBox_Page = TextBoxPage(context.driver)

def after_scenario(context, scenario):
    """Se ejecuta después de cada escenario"""
    context.driver.close()

def after_all(context):
    """Se ejecuta después de todas las pruebas, cierra el WebDriver."""
    context.driver.quit()
