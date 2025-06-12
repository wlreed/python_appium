from config import *

@pytest.mark.usefixtures("appium_service", "appium_driver")
class BaseTest:
    pass
