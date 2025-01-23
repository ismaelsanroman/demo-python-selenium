from behave import step

@step("interactúa con el formulario de registro")
def user_interacts_with_form(context):
    for row in context.table:
        # 🔹 Guardamos los valores en context para usarlos en el siguiente step
        context.full_name = row["full_name"]
        context.email = row["email"]
        context.current_address = row["current_address"]
        context.permanent_address = row["permanent_address"]

        context.TextBox_Page.fill_text_box(context.full_name, context.email, context.current_address, context.permanent_address)
        context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        context.TextBox_Page.click_elements(context.TextBox_Page.submit_button)

@step("el formulario es enviado correctamente")
def form_is_submitted(context):
    expected_values = {
        "full_name": context.full_name,
        "email": context.email,
        "current_address": context.current_address,
        "permanent_address": context.permanent_address
    }
    
    context.TextBox_Page.validate_form_submission(expected_values)
