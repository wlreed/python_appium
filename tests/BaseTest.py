from config import *

@pytest.mark.usefixtures("appium_service", "new_appium_driver") # "appium_driver")
class BaseTest:
    pass
