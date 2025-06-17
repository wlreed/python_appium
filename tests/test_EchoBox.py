from screens import *
from config import *
from BaseTest import BaseTest

@pytest.mark.echobox
class TestEchoBox(BaseTest):  
    def test_click_echo_box(appium_service, new_appium_driver):
        hs = HomeScreen()
        echo_box_element = hs.echo_box_element()
        hs.click(echo_box_element)
        es = EchoBoxScreen()
        back_button = es.back_button_element()
        es.click(back_button)
        
