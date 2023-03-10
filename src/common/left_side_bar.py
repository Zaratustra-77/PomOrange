from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.shared.left_side_bar_locators import Left_side_bar_locators as LSB


class LeftSideBar:

    def __init__(self, driver):
        self.driver = driver

    # # # # locatorss # # # #
    def get_att_admin(self):
        admin = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.admin_xpath))).get_attribute('text')
        return admin
    def get_att_pim(self):
        pim = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.pim_text))).get_attribute('text')
        return pim
    def get_att_leave(self):
        leave = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.leave_text))).get_attribute('text')
        return leave
    def get_att_time(self):
        time = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.time_text))).get_attribute('text')
        return time
    def get_att_recruitment(self):
        recruitment =WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.recruitment_text))).get_attribute('text')
        return recruitment

    def get_att_my_info(self):
        my_info = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.my_info_text))).get_attribute('text')
        return my_info
    def get_att_performance(self):
        performance = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.performance_text))).get_attribute('text')
        return performance
    def get_att_dashboard(self):
        dashboard = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.dashboard_text))).get_attribute('text')
        return dashboard
    def get_att_directory(self):
        directory = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.directory_text))).get_attribute('text')
        return directory
    def get_att_maintenance(self):
        maintenance = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.maintenance_text))).get_attribute('text')
        return maintenance
    def get_att_buzz(self):
        buzz = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,LSB.buzz_text))).get_attribute('text')
        return buzz




    # # # # Actions # # # #

    def click_admin(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.admin_xpath))).click()

    def click_pim(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.pim_text))).click()

    def click_leave(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.leave_text))).click()

    def click_time(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.time_text))).click()

    def click_recruitment(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.recruitment_text))).click()

    def click_my_info(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.my_info_text))).click()

    def click_performance(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.performance_text))).click()

    def click_dashboard(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.dashboard_text))).click()

    def click_directory(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.directory_text))).click()

    def click_maintenance(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.maintenance_text))).click()

    def click_buzz(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, LSB.buzz_text))).click()

