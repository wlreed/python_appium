from config import *

from screens.Screen import Screen

class HomeScreen(Screen):

    def __init__(self):
        LOG.info("instantiating HomeScreen")
        self.string_map = dict(
            echo_box = "Echo Box",
            login = "Login Screen",
            back_button_id = "Navigate Up",
            back_button_predicate = "name == \"TheApp\" AND label == \"TheApp\" "
    + "AND type == \"XCUIElementTypeButton\"",
            clipboard = "Clipboard Demo",
            webview = "Webview Demo",
            dual_webview = "Dual Webview Demo",
            list = "List Demo",
            photo = "Photo Demo",
            geolocation = "Geolocation Demo",
            picker = "Picker Demo"
        )
        super().__init__

    def echo_box_element(self):
        return self.find_element_by_id(self.string_map['echo_box'])

    def login_element(self):
        return self.find_element_by_id(self.string_map['login'])
    
    def clipboard_element(self):
        return self.find_element_by_id(self.string_map['clipboard'])
    
    def webview_element(self):
        return self.find_element_by_id(self.string_map['webview'])
    
    def dual_webview_element(self):
        return self.find_element_by_id(self.string_map['dual_webview'])
    
    def list_element(self):
        return self.find_element_by_id(self.string_map['list'])
    
    def photo_element(self):
        return self.find_element_by_id(self.string_map['photo'])
    
    def geolocation_element(self):
        return self.find_element_by_id(self.string_map['geolocation'])
    
    def picker_element(self):
        return self.find_element_by_id(self.string_map['picker'])
