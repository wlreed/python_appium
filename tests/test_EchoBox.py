from screens import *
from config import *
from BaseTest import BaseTest

@pytest.mark.configed  
def test_click_echo_box(appium_service, appium_driver):
    hs = HomeScreen(appium_driver)
    echo_box_element = hs.echo_box_element()
    hs.click(echo_box_element)
    time.sleep(10)

class test_EchoBox(BaseTest):
    @pytest.mark.configed
    @pytest.mark.usefixtures("appium_driver")   
    def test_click_echo_box(self):
        hs = HomeScreen(self.driver)
        self.driver.click(hs.echo_box_element)
        
