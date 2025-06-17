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

    def test_click_webview_demo(appium_service, new_appium_driver):
        hs = HomeScreen()
        webview_element = hs.webview_element()
        hs.click(webview_element)
        ws = WebviewScreen()
        back_button = ws.back_button_element()
        ws.click(back_button)

    def test_click_dual_webview_demo(appium_service, new_appium_driver):
        hs = HomeScreen()
        dual_webview_element = hs.dual_webview_element()
        hs.click(dual_webview_element)
        dws = DualWebviewScreen()
        back_button = dws.back_button_element()
        dws.click(back_button)

    def test_click_list_demo(appium_service, new_appium_driver):
        hs = HomeScreen()
        list_element = hs.list_element()
        hs.click(list_element)
        ls = ListScreen()
        back_button = ls.back_button_element()
        ls.click(back_button)

    def test_click_photo_demo(appium_service, new_appium_driver):
        hs = HomeScreen()
        photo_element = hs.list_element()
        hs.click(photo_element)
        ps = PhotoScreen()
        back_button = ps.back_button_element()
        ps.click(back_button)

    @pytest.mark.skip("This test needs work")  # TODO: getting alert screen for location permission
    def test_click_geolocation_demo(appium_service, new_appium_driver):
        hs = HomeScreen()
        geolocation_element = hs.geolocation_element()
        hs.click(geolocation_element)
        gs = GeolocationScreen()
        back_button = gs.back_button_element()
        gs.click(back_button)

    def test_click_picker_demo(appium_service, new_appium_driver):
        hs = HomeScreen()
        picker_element = hs.picker_element()
        hs.click(picker_element)
        ps = PickerScreen()
        back_button = ps.back_button_element()
        ps.click(back_button)
