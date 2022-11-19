from behave import *
from Locators import locators
from Helper.SeleniumHelper import SeleniumHelper
from Logs import logs_file
login_url = "https://www.facebook.com/login/"

log = logs_file.get_logs()

@when('user input wrong credentials')
def step_impl(context):
    SeleniumHelper(context.driver).open_page(login_url)
    log.info("Page Opened")
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_login, "anshul123.io")
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_password, "anshul123.io")
    log.info("Password entered")
    SeleniumHelper(context.driver).click(locators.button_login)
    log.info("Login Button Clicked")


@then('Error message will come')
def step_impl(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(locators.link_login_error_message)
