from tests.test_login_page import TestOH
from tests.test_dash_page import TestOHDash
from tests.test_left_side_bar import TestLeftSB
class TestCombined(TestOH, TestOHDash,TestLeftSB):
    pass
