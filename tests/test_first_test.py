#!/usr/bin/env python
"""
POC Appium tests
"""

# Python/Pytest
import time
import json

from config import *

from appium.webdriver.common.appiumby import AppiumBy
from local_libs import *

@pytest.mark.ios
def test_ios_click(appium_service, ios_driver_factory):
    """
    Usage of the context manager ensures the driver session is closed properly
    after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    """
    with ios_driver_factory({
        'appium:automationName': 'XCUITest',
        'appium:platformName': 'iOS',
        'appium:platformVersion': '17.2',
        'appium:deviceName': 'iPhone 15',
        'appium:app': 'apps/TheApp.app.zip',
        'appium:maxTypingFrequency': '10',
        'appium:connectHardwareKeyboard': True
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Login Screen')
        el.click()

@pytest.mark.android
def test_android_click(appium_service, android_driver_factory):
    """
    Usage of the context manager ensures the driver session is closed properly
    after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    """
    with android_driver_factory({
        'appium:automationName': 'uiautomator2',
        'appium:platformName': 'android',
        'appium:platformVersion': '10',
        'appium:avd': 'Pixel_6_API_31',
        'appium:avdLaunchTimeout': '8000',
        'appium:avdReadyTimeout': '400',
        'appium:app': 'apps/TheApp.apk'
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Login Screen')
        el.click()
        time.sleep(1)

@pytest.mark.configed
def test_configed_click(appium_service, android_driver_factory, ios_driver_factory):
    LOG.info("CONFIG TESTS")
    LOG.info(f"settings: {json.dumps(SETTINGS.configs['appium'])}")
    appium_settings = SETTINGS.configs['appium']
    LOG.info(f"currently testing {appium_settings['appium:automationName']}")
    if (appium_settings['appium:automationName'] == 'uiautomator2'):
        with android_driver_factory(
            json.dumps(SETTINGS.configs['appium'])
            ) as driver:
            el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Login Screen')
            el.click()
            time.sleep(1)
    elif (appium_settings['appium:automationName'] == 'XCUITest'):
        with ios_driver_factory(
            json.dumps(SETTINGS.configs['appium'])
            ) as driver:
            el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Login Screen')
            el.click()
            time.sleep(1)


@pytest.mark.test
def test_test_click(appium_service):
    LOG.info("What's up Doc?")
    LOG.debug("Debugging!")
    LOG.warn("Warning!!!1")
