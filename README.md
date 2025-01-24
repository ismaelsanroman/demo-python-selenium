# 🧪 Demo Automation Testing con Python, Selenium y Cucumber

## 📌 Descripción
Este proyecto automatiza la interacción con la página [DemoQA](https://demoqa.com/) utilizando **Selenium** y **Behave** (BDD con Python). Además, los reportes de pruebas se generan con **Allure** para visualizar los resultados de manera gráfica.

---

## 🚀 Tecnologías utilizadas

🔹 **Python** (Lenguaje principal)  
🔹 **Behave** (Framework BDD)  
🔹 **Selenium** (Automatización del navegador)  
🔹 **Allure** (Reportes visuales)  
🔹 **WebDriver Manager** (Manejo de drivers de Selenium)  

---

## 📂 Estructura del proyecto
```
📦 demo-python-selenium
├── 📂 .github               # Configuración de GitHub (acciones, workflows, etc.)
├── 📂 .idea                 # Configuración de JetBrains (PyCharm)
├── 📂 .vscode               # Configuración de VS Code
├── 📂 allure-report         # Reportes generados por Allure
├── 📂 features              # Escenarios de prueba en Gherkin
│   ├── 📂 steps             # Implementación de los steps en Python
│   │   ├── demoqa_steps.py
│   │   ├── textbox_steps.py
│   │   ├── environment.py   # Configuración global de Behave
│   ├── google_search.feature
├── 📂 pages                 # Page Object Model (POM) para las páginas web
│   ├── textbox_page.py
├── 📂 reports               # Resultados y reportes de pruebas
│   ├── allure-report
│   ├── allure-results
├── 📂 venv                  # Entorno virtual de Python
├── .gitignore               # Archivos ignorados por Git
├── behave.ini               # Configuración de Behave
├── conftest.py              # Configuración de pytest (si se usa)
├── pretty.output            # Salida formateada (quizás logs o resultados de pruebas)
├── README.md                # 📖 Documentación del proyecto
├── requirements.txt         # 📦 Dependencias del proyecto
```

---

## ⚙️ Instalación
### 🔹 1. Clonar el repositorio
```sh
git clone https://github.com/ismaelsanroman/demo-python-selenium.git
cd demo-python-selenium
```

### 🔹 2. Crear un entorno virtual
```sh
python -m venv venv
```
Activa el entorno:
- **Windows:**  
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**  
  ```sh
  source venv/bin/activate
  ```

### 🔹 3. Instalar dependencias
```sh
pip install -r requirements.txt
```

---

## 🏃‍♂️ Ejecución de las pruebas
### 🔹 1. Ejecutar los tests con Behave
```sh
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

### 🔹 2. Generar el reporte de Allure
```sh
allure generate reports/allure-results -o reports/allure-report --clean
```

### 🔹 3. Abrir el reporte en el navegador
```sh
allure open reports/allure-report
```
Si esto no funciona, abre manualmente `index.html` dentro de `reports/allure-report`.

---

## ✨ Ejemplo de Escenario
Archivo: **`features/google_search.feature`**
```gherkin
Feature: Rellenamos el formulario de TextBox

  Scenario: Rellenamos el formulario de TextBox
    Given el usuario está en la página de DemoQA
    And clicamos sobre el apartado "Elements"
    And nos dirigimos a "Text Box"
    When interactúa con el formulario de registro
      | full_name       | email              | current_address  | permanent_address |
      | Ismael Sanromán | isanroman@sdet.com | Calle SDET, 1    | Calle prueba, 2   |
    Then el formulario es enviado correctamente
```

---

## 📌 Notas importantes
1️⃣ **Allure CLI** debe estar instalado para generar reportes. Instálalo con:
   ```sh
   scoop install allure  # Windows (Scoop)
   brew install allure   # macOS (Homebrew)
   ```
   O descárgalo desde: [https://github.com/allure-framework/allure2/releases](https://github.com/allure-framework/allure2/releases)

2️⃣ Si el reporte de Allure no se abre correctamente, intenta borrar los resultados previos:
   ```sh
   rm -rf reports/allure-results/*
   ```

3️⃣ **Drivers de Selenium:** WebDriver Manager se encarga automáticamente de los drivers. No es necesario descargarlos manualmente.

---

## 📌 Contacto
[📧 Email](mailto:ismaelsanromansanchez@gmail.com)  
[🤖 GitHub:](https://github.com/ismaelsanroman) 
