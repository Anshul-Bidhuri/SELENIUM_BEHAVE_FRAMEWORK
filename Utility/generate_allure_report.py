import os


def generate_allure_report():
    """This method generates allure report from the allure results"""
    os.chdir(os.path.abspath(__file__+"/../../"))
    os.popen(r'allure generate Report\allure_result -o Report\allure_report --clean').read()


generate_allure_report()