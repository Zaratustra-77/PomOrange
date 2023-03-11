from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.shared.left_side_bar_locators import Left_side_bar_locators as LSB


class LeftSideBar:

    def __init__(self, driver):
        self.driver = driver
        self.menu_options = {
            'Admin': LSB.admin_xpath,
            'PIM': LSB.pim_xpath,
            'Leave': LSB.leave_xpath,
            'Time': LSB.time_xpath,
            'Recruitment': LSB.recruitment_xpath,
            'My Info': LSB.my_info_xpath,
            'Performance': LSB.performance_xpath,
            'Dashboard': LSB.dashboard_xpath,
            'Directory': LSB.directory_xpath,
            'Maintenance': LSB.maintenance_xpath,
            'Buzz': LSB.buzz_xpath
        }
    # # # # Actions # # # #


    def click_admin(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.admin_xpath))).click()

    def click_pim(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.pim_xpath))).click()

    def click_leave(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.leave_xpath))).click()

    def click_time(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.time_xpath))).click()

    def click_recruitment(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.recruitment_xpath))).click()

    def click_my_info(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.my_info_xpath))).click()

    def click_performance(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.performance_xpath))).click()

    def click_dashboard(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.dashboard_xpath))).click()

    def click_directory(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.directory_xpath))).click()

    def click_maintenance(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.maintenance_xpath))).click()

    def click_buzz(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LSB.buzz_xpath))).click()

    def menu_list(self):
        return LSB.menu_list

    def maintenance_visible(self):
        visible = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,LSB.maintenance_new_window_xpath)))
        return visible
    def click_menu_options(self,option):
        locator = self.menu_options[option]
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, locator))).click()
