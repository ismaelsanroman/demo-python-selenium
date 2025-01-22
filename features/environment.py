from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def before_all(context):
    """Se ejecuta antes de todas las pruebas, inicializa el WebDriver."""
    options = Options()
    # options.add_argument("--headless")  # Opcional, quitar si quieres ver la ejecución
    options.add_argument("--start-maximized")  # Maximizar ventana para evitar problemas
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

def after_all(context):
    """Se ejecuta después de todas las pruebas, cierra el WebDriver."""
    context.driver.quit()
