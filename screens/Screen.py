from config import *
from appium.webdriver.common.appiumby import AppiumBy

class Screen:

    def __new__(cls):
        if cls is Screen:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls)
    
    def __init__(): #, driver):
        pass #self.driver = driver

    def click(self, element):
        LOG.info(f"clicking element: {element.text}")
        element.click()
    
    def send_keys(self, locator, content):
        if str(locator).endswith("_XPATH"):
            APM.driver.find_element(by=AppiumBy.XPATH, value=locator)\
                .send_keys(content)
            APM.driver.hide_keyboard()
        if str(locator).endswith("_TEXT"):
            APM.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=locator)\
                .send_keys(content)
            APM.driver.hide_keyboard()
            