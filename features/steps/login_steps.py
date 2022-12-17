from behave import *
from Locators import locators
from Helper.SeleniumHelper import SeleniumHelper
from Logs import logs_file
from TestData import test_data

log = logs_file.get_logs()

@when('user input wrong credentials')
def step_impl(context):
    SeleniumHelper(context.driver).open_page(test_data.facebook_login_url)
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_login, test_data.correct_login_id)
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_password, test_data.incorrect_login_password)
    SeleniumHelper(context.driver).click(locators.button_login)


@then('Error message will come')
def step_impl(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(locators.link_login_error_message)
