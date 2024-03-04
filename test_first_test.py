#!/usr/bin/env python

# Python/Pytest
import pytest
import time

from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.ios
def test_ios_click(appium_service, ios_driver_factory):
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with ios_driver_factory({
        'appium:automationName': 'XCUITest',
        'appium:platformName': 'iOS',
        'appium:deviceName': 'iPhone 15',
        'appium:app': 'apps/TheApp.app.zip',
        'appium:maxTypingFrequency': '10',
        'appium:connectHardwareKeyboard': True
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Login Screen')
        el.click()

@pytest.mark.android
def test_android_click(appium_service, android_driver_factory):
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with android_driver_factory({
        'appium:automationName': 'UiAutomator2',
        'appium:platformName': 'Android',
        'appium:deviceName': 'Pixel 6 API 31',
        'appium:app': 'apps/TheApp.apk',
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Login Screen')
        el.click()
        time.sleep(1)
