from src.utils.webdriverSetUp import WebDriverSetup


class TestOH(WebDriverSetup):

    def test_1_valid_login(self):
        self.login_page.set_username('Admin')
        self.login_page.set_password('admin123')
        self.login_page.click_login()
        assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    def test_2_invalid_login(self):
        self.login_page.set_username('min')
        self.login_page.set_password('admin123')
        self.login_page.click_login()
        assert self.driver.current_url ==  'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'



