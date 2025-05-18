"""
Config file for python appium testing
"""
import datetime
import logging
from pathlib import Path
import pytest
from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'
TIMESTAMP = f'{datetime.datetime.now():%h-%d_%H.%M.%S}'


Path('results/' + TIMESTAMP).mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO, filename='results/' + TIMESTAMP + '/pytest.txt',
                    filemode='w')
log = logging.getLogger("log").setLevel('INFO')
logging.propagate=True

@pytest.fixture(scope='session')
def appium_service():
    """
    Starts the Appium server and logs all output to a file
    """
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT), '--log',
              'results/' + TIMESTAMP + '/appium_server_log.txt'],
        timeout_ms=20000,
    )
    yield service
    service.stop()


def create_ios_driver(custom_opts = None):
    """
    Creates ios driver with capabilities specified
    """
    options = XCUITestOptions()
    options.platformVersion = '17.2'
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


def create_android_driver(custom_opts = None):
    """
    Creates android driver with capabilities specified
    """
    options = UiAutomator2Options()
    options.platformVersion = '10'
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


@pytest.fixture
def ios_driver_factory():
    """
    Returns ios driver
    """
    return create_ios_driver


@pytest.fixture
def ios_driver():
    """
    Simpler ios driver
    """
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_ios_driver()
    yield driver
    driver.quit()


@pytest.fixture
def android_driver_factory():
    """
    Returns android driver
    """
    return create_android_driver


@pytest.fixture
def android_driver():
    """
    Simpler android driver
    """
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_android_driver()
    yield driver
    driver.quit()
