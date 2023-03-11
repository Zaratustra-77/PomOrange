from src.utils.webdriverSetUp import WebDriverSetup
from selenium.common.exceptions import TimeoutException

class TestLeftSB(WebDriverSetup):

    def test_left_side_bar(self):
        self.login_page.set_username('Admin')
        self.login_page.set_password('admin123')
        self.login_page.click_login()
        assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        header = self.dashboard_page.verify_header_title()
        self.assertEqual(header,'Dashboard')
        for item in self.left_side_bar.menu_list():
            if item == 'My Info':
                self.left_side_bar.click_menu_options(item)
                header = self.dashboard_page.verify_header_title()
                self.assertEqual(header, 'PIM')
            elif item == 'Maintenance':
                self.left_side_bar.click_menu_options(item)
                pop_up = self.left_side_bar.maintenance_visible()
                self.assertTrue(pop_up)
            else:
                self.left_side_bar.click_menu_options(item)
                self.driver.implicitly_wait(2)
                header = self.dashboard_page.verify_header_title()
                self.assertEqual(header, item)



