import unittest
import HtmlTestRunner
from tests import test_login_page,test_dash_page,test_left_side_bar

from src.utils.webdriverSetUp import WebDriverSetup

class MyTestSuite(WebDriverSetup):
    def test_suite(self):
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_login_page)
        suite.addTests(loader.loadTestsFromModule(test_dash_page))
        suite.addTests(loader.loadTestsFromModule(test_left_side_bar))

        return suite

if __name__ == '__main__':
    suite = MyTestSuite().test_suite()
    runner = HtmlTestRunner.HTMLTestRunner(output='reports')
    runner.run(suite)
