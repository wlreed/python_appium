from config import *
from appium.webdriver.common.appiumby import AppiumBy

class Screen:

    def __new__(cls, screen):
        if cls is Screen:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls)
    
    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        LOG.info(f"clicking element: {element.text}")
        element.click()
    
    def send_keys(self, locator, content):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=AppiumBy.XPATH, value=locator)\
                .send_keys(content)
            self.driver.hide_keyboard()
        if str(locator).endswith("_TEXT"):
            self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=locator)\
                .send_keys(content)
            self.driver.hide_keyboard()
            