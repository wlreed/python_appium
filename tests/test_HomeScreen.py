from screens import *
from config import *
from BaseTest import BaseTest

@pytest.mark.homescreen
class TestHomeScreen(BaseTest):  
    def test_click_echo_box(appium_service, new_appium_driver):
        hs = HomeScreen()
        echo_box_element = hs.echo_box_element()
        hs.click(echo_box_element)
