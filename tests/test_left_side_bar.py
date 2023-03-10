from src.utils.webdriverSetUp import WebDriverSetup

class TestLeftSB(WebDriverSetup):

    def test_left_side_bar(self):
        self.login_page.set_username('Admin')
        self.login_page.set_password('admin123')
        self.login_page.click_login()
        assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        header = self.dashboard_page.verify_header_title()
        self.assertTrue(header,'Dashboard')
        self.left_side_bar.click_admin()
        self.assertTrue(self.dashboard_page.verify_header_title(),'Admin / User Management')
        self.left_side_bar.click_pim()
        self.assertTrue(self.dashboard_page.verify_header_title(),'PIM')
