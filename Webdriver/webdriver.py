from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_chrome_webdriver():
    driver = webdriver.Chrome(service=Service("chromedriver_108.exe"))
    return driver
