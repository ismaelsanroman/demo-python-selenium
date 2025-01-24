Feature: Rellenamos el formulario de TextBox

  Scenario: Rellenamos el formulario de TextBox
    Given el usuario está en la página de DemoQA
    And clicamos sobre el apartado "Elements"
    And nos dirigimos a "Text Box"
    When interactúa con el formulario de registro
      | full_name       | email              | current_address | permanent_address |
      | Ismael Sanromán | isanroman@sdet.com | Calle SDET, 1   | Calle prueba, 2   |
    Then el formulario es enviado correctamente
