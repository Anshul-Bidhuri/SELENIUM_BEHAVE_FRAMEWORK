from Webdriver import webdriver
from Logs import logs_file

log = logs_file.get_logs()

def before_scenario(context, scenario):
    log.info("Chrome Driver Executed")
    context.driver = webdriver.get_chrome_webdriver()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    log.info("Chrome Driver Closed")
    context.driver.close()
