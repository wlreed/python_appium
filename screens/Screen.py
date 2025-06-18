from config import *
from appium.webdriver.common.appiumby import AppiumBy

class Screen:
    page_source = ""

    def __new__(cls):
        if cls is Screen:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls)
    
    def __init__(self):
        LOG.info(f"Instantiating: {self.__module__[8:]}")
        self.page_source = self.get_page_source()

    def click(self, element):
        if (APM.automation_name == 'uiautomator2'):
            LOG.info(f"clicking element: {element.tag_name}")
        elif (APM.automation_name == 'XCUITest'):
            LOG.info(f"clicking element: {element.text}")
        element.click()

    def find_element_by_id(self, id):
        return APM.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, 
                                       value=id)
    
    def find_element_by_ios_predicate(self, predicate):
        return APM.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=predicate)
    
    def get_page_source(self):
        return APM.driver.page_source
    
    def send_keys(self, locator, content):
        if str(locator).endswith("_XPATH"):
            APM.driver.find_element(by=AppiumBy.XPATH, value=locator)\
                .send_keys(content)
            APM.driver.hide_keyboard()
        if str(locator).endswith("_TEXT"):
            APM.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=locator)\
                .send_keys(content)
            APM.driver.hide_keyboard()
            