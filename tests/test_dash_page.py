from src.utils.webdriverSetUp import WebDriverSetup

class TestOHDash(WebDriverSetup):

    def test_dashboard_header(self):
        self.login_page.set_username('Admin')
        self.login_page.set_password('admin123')
        self.login_page.click_login()
        assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        element = self.dashboard_page.verify_header_title()
        self.assertTrue(element,'Dashboard')



