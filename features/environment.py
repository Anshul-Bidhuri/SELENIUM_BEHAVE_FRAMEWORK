from Webdriver import webdriver
import logging

def before_scenario(context, scenario):
    context.driver = logging.FileHandler.selenium_driver = webdriver.get_chrome_webdriver()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.close()
