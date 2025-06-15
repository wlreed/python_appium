from config import *
from appium.webdriver.common.appiumby import AppiumBy

from screens.Screen import Screen

class HomeScreen(Screen):
    driver = None

    def __init__(self):
        LOG.info("instantiating HomeScreen")
        self.driver = APM.driver
        super().__init__
        LOG.info(f"driver: {APM.driver}")
        LOG.info(f"driver methods: {APM.driver.__dict__}")

    def echo_box_element(self):
        return APM.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Echo Box')
