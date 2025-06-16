from screens import *
from config import *
from BaseTest import BaseTest

@pytest.mark.homescreen
class TestHomeScreen(BaseTest):  
    def test_click_echo_box(appium_service, new_appium_driver):
        hs = HomeScreen()
        echo_box_element = hs.echo_box_element()
        hs.click(echo_box_element)
        es = EchoBoxScreen()
        back_button = es.back_button_element()
        es.click(back_button)

    def test_click_login(appium_service, new_appium_driver):
        hs = HomeScreen()
        login_element = hs.login_element()
        hs.click(login_element)
        ls = LoginScreen()
        back_button = ls.back_button_element()
        ls.click(back_button)

    def test_click_clipboard_demo(appium_service, new_appium_driver):
        hs = HomeScreen()
        clipboard_element = hs.clipboard_element()
        hs.click(clipboard_element)
        cs = ClipboardScreen()
        back_button = cs.back_button_element()
        cs.click(back_button)
