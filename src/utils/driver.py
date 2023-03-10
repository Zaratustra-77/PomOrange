from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_chrome_driver():
    chromedriver_path = "C:/Webdriver/chromedriver.exe"
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=service, options=options)

    return driver
