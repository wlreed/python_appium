from config import *

from screens.Screen import Screen

class SecondaryScreen(Screen):
    def __new__(cls):
        if cls is Screen:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls)

    def __init__(self):
        super().__init__()
        self.string_map = dict(
            back_button_id = "Navigate Up",
            back_button_predicate = "name == \"TheApp\" AND label == \"TheApp\" "
    + "AND type == \"XCUIElementTypeButton\""
        )

    def back_button_element(self):
        if (APM.automation_name == 'XCUITest'):
            return self.find_element_by_ios_predicate(self.string_map['back_button_predicate'])
        elif (APM.automation_name == 'uiautomator2'):
            return self.find_element_by_id(self.string_map['back_button_id'])
