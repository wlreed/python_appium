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
    SETTINGS.__new__(SETTINGS)
    driver = None

    def __new__(self):
        super.__call__(self)
        appium_settings = SETTINGS.configs['appium']
        LOG.info(f"currently testing {appium_settings['appium:automationName']}")
        capabilities = json.dumps(appium_settings)
        LOG.info(f"capabilities: {capabilities}")
        if (appium_settings['appium:automationName'] == 'uiautomator2'):
            self.driver = webdriver.Remote(f'http://{self.APPIUM_HOST}:{self.APPIUM_PORT}',
                              options=UiAutomator2Options().load_capabilities(json.loads(capabilities)))
        else:
            self.driver = webdriver.Remote(f'http://{self.APPIUM_HOST}:{self.APPIUM_PORT}',
                              options=XCUITestOptions().load_capabilities(json.loads(capabilities)))
        self.driver.implicitly_wait(10)

        return self.driver
