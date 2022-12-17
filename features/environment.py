from Webdriver import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.get_chrome_webdriver()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.close()
