Feature: DemoQA Text-Box

  Scenario: Rellenamos el formulario de TextBox
    Given el usuario está en la página de DemoQA
    And clicamos sobre el apartado "Elements"
    And nos dirigimos a "Text Box"
    When interactúa con el formulario de registro
      | first_name | last_name |
      | Ismael     | García    |
    Then el formulario es enviado correctamente
