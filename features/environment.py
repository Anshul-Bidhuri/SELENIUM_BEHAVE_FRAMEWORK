from Webdriver import webdriver
import logging


def before_all(context):
    browser_type = context.config.userdata.get("browser")
    context.browser_type = browser_type


def before_scenario(context, scenario):
    context.driver = logging.FileHandler.selenium_driver = webdriver.get_webdriver(context.browser_type)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.close()
