import time

from config import *
from appium.webdriver.common.appiumby import AppiumBy

from screens.Screen import Screen

class HomeScreen(Screen):

    def __init__(self, driver):
        LOG.info("instantiating HomeScreen")
        self.driver = driver
        super().__init__(driver)

    def echo_box_element(self):
        return self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Echo Box')
    
    def click_echo_box_element(self):
        LOG.info(f"Clicking Echo Box")
        return self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Echo Box').click()
