from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.shared.left_side_bar_locators import Left_side_bar_locators as LSB


class LeftSideBar:

    def __init__(self, driver):
        self.driver = driver

    # # # # Actions # # # #

    def click_admin(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.admin_xpath))).click()

    def click_pim(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.pim_xpath))).click()

    def click_leave(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.leave_text))).click()

    def click_time(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.time_text))).click()

    def click_recruitment(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.recruitment_text))).click()

    def click_my_info(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.my_info_text))).click()

    def click_performance(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.performance_text))).click()

    def click_dashboard(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.dashboard_text))).click()

    def click_directory(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.directory_text))).click()

    def click_maintenance(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.maintenance_text))).click()

    def click_buzz(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.buzz_text))).click()

