from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.login_pag_locators import LoginLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver


    # # # # Actions # # # #


    def set_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LoginLocators.user_name_text))).send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LoginLocators.password_text))).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,LoginLocators.login_xpath))).click()


