from screens import *
from config import *
from BaseTest import BaseTest

@pytest.mark.homescreen
class TestHomeScreen(BaseTest):
    #@pytest.mark.homescreen  
    def test_click_echo_box(appium_service, new_appium_driver):
        hs = HomeScreen(APM.driver)
        echo_box_element = hs.echo_box_element()
        hs.click(echo_box_element)
