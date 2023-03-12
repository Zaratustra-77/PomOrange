import time
import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.common.left_side_bar import LeftSideBar
from selenium.webdriver.chrome.options import Options


class WebDriverSetup(unittest.TestCase):
    def setUp(self) -> None:
        try:
            chromedriver_path = "C:/Webdriver/chromedriver.exe"
            service = Service(executable_path=chromedriver_path)
            options = Options()
            options.headless = False
            # options = webdriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(service=service,options=options)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.login_page = LoginPage(self.driver)
            self.dashboard_page = DashboardPage(self.driver)
            self.left_side_bar = LeftSideBar(self.driver)
            time.sleep(1)


        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Elik/PycharmProjects/seleniumProjects/POM_Orange/reports'))

