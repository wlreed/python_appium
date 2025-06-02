"""
Config file for python appium testing
"""
import datetime
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService

from config import *

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'
TIMESTAMP = f'{datetime.datetime.now():%h-%d_%H.%M.%S}'

Path('results/' + TIMESTAMP).mkdir(parents=True, exist_ok=True)
LOG.__call__(LOG, TIMESTAMP)
SETTINGS.__call__(SETTINGS)

@pytest.fixture(scope='session')
def appium_service():
    """
    Starts the Appium server and logs all output to a file
    """
    LOG.info("Starting Appium Service")
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

# For Page Obj Test
@pytest.fixture(scope="function")
def appium_driver(request):
    driver = None
    appium_settings = SETTINGS.configs['appium']
    LOG.info(f"currently testing {appium_settings['appium:automationName']}")
    capabilities = json.dumps(appium_settings)
    LOG.info(f"capabilities: {capabilities}")
    if (appium_settings['appium:automationName'] == 'uiautomator2'):
        driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}',
                              options=UiAutomator2Options().load_capabilities(json.loads(capabilities)))
    else:
        driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}',
                              options=XCUITestOptions().load_capabilities(json.loads(capabilities)))
    driver.implicitly_wait(10)
    
    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver

def create_ios_driver(custom_opts = None):
    """
    Creates ios driver with capabilities specified
    """
    options = XCUITestOptions()
    if custom_opts is not None:
        options.load_capabilities(json.loads(custom_opts))
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

def create_android_driver(custom_opts = None):
    """
    Creates android driver with capabilities specified
    """
    options = UiAutomator2Options()
    if custom_opts is not None:
        options.load_capabilities(json.loads(custom_opts))
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
