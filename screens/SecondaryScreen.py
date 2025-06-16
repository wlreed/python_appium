from config import *

from screens.Screen import Screen

class SecondaryScreen(Screen):
    def __init__(self):
        LOG.info("instantiating HomeScreen")
        self.string_map = dict(
            back_button_id = "Navigate Up",
            back_button_predicate = "name == \"TheApp\" AND label == \"TheApp\" "
    + "AND type == \"XCUIElementTypeButton\""
        )
        super().__init__

    def back_button_element(self):
        if (APM.automation_name == 'XCUITest'):
            return self.find_element_by_ios_predicate(self.string_map['back_button_predicate'])
        elif (APM.automation_name == 'uiautomator2'):
            return self.find_element_by_id(self.string_map['back_button_id'])
