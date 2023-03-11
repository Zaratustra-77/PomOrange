from src.utils.webdriverSetUp import WebDriverSetup

class TestLeftSB(WebDriverSetup):

    def test_left_side_bar(self):
        self.login_page.set_username('Admin')
        self.login_page.set_password('admin123')
        self.login_page.click_login()
        assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        header = self.dashboard_page.verify_header_title()
        self.assertEqual(header,'Dashboard')
        self.left_side_bar.click_admin()
        header = self.dashboard_page.verify_header_title()
        self.assertEqual(header, "AdminUser Management", 'element not found')
        self.left_side_bar.click_pim()
        header = self.dashboard_page.verify_header_title()
        self.assertEqual(header,'PIM')
        # self.left_side_bar.click_leave()
        # self.assertEqual(header,'Leave')
        #
        # self.left_side_bar.click_pim()
        # self.left_side_bar.click_pim()
        # self.left_side_bar.click_pim()
        # self.left_side_bar.click_pim()
        #
