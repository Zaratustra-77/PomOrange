from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.dashboard_locators import DashboardLocators
class DashboardPage:


    def __init__(self,driver):
        self.driver = driver

    def verify_header_title(self):
        header_title_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,DashboardLocators.header_title_locator))).get_attribute('textContent')

        return header_title_text
