from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from .Singleton import Singleton
from .Settings import Settings as SETTINGS
from .Logger import Logger as LOG

from config import *

"""Class to represent the appium driver"""
class APM():
    APPIUM_PORT = 4723
    APPIUM_HOST = '127.0.0.1'
    SETTINGS.__call__(SETTINGS)
    driver = None
    automation_name = ""

    def __call__(self):
        super.__call__(self)
        if (self.driver == None):
            appium_settings = SETTINGS.configs['appium']
            self.automation_name = appium_settings['appium:automationName']
            LOG.info(f"currently testing {self.automation_name}")
            capabilities = json.dumps(appium_settings)
            LOG.info(f"capabilities: {capabilities}")
            if (self.automation_name == 'uiautomator2'):
                self.driver = webdriver.Remote(f'http://{self.APPIUM_HOST}:{self.APPIUM_PORT}',
                              options=UiAutomator2Options().load_capabilities(json.loads(capabilities)))
            elif (self.automation_name == 'XCUITest'):
                self.driver = webdriver.Remote(f'http://{self.APPIUM_HOST}:{self.APPIUM_PORT}',
                              options=XCUITestOptions().load_capabilities(json.loads(capabilities)))
            else:
                raise TypeError(f"Don't know how to test {self.automation_name}")

            self.driver.implicitly_wait(10)
        return self.driver
