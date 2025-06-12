from screens import *
from config import *
from BaseTest import BaseTest

@pytest.mark.homescreen
class TestHomeScreen(BaseTest):
    #@pytest.mark.homescreen  
    def test_click_echo_box(appium_service, appium_driver):
        hs = HomeScreen(appium_driver)
        echo_box_element = hs.echo_box_element()
        hs.click(echo_box_element)
