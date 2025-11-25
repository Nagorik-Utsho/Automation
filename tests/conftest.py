import subprocess
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.vpn_activity import logout, onboarding


def get_connected_device_info():
    """
    Detects connected Android devices and fetches UDID and Android version.
    Returns the first device found.
    """
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')[1:]  # Skip header
    devices = [line.split('\t')[0] for line in lines if 'device' in line]

    if not devices:
        raise Exception("No connected Android devices found.")

    device_udid = devices[0]

    result_version = subprocess.run(
        ['adb', '-s', device_udid, 'shell', 'getprop', 'ro.build.version.release'],
        capture_output=True, text=True
    )
    android_version = result_version.stdout.strip()

    return device_udid, android_version

@pytest.fixture(scope="session")
def driver():
    """
    Pytest fixture to initialize Appium driver.
    """
    device_udid, android_version = get_connected_device_info()

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = android_version
    options.device_name = device_udid
    options.automation_name = "UiAutomator2"
    options.no_reset = True
    options.new_command_timeout = 300
    options.auto_grant_permissions = True
    options.ensure_webviews_have_pages = True
    options.dont_stop_app_on_reset = True

    # Replace with your app info
    options.app_package = "com.enovavpn.mobile"
    options.app_activity = "com.enovavpn.mobile.MainActivity"

    driver_instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    print("Driver setup successful for device:", driver_instance.capabilities['deviceName'])

    yield driver_instance  # Provide the driver to tests

    driver_instance.quit()  # Cleanup after all tests


@pytest.fixture
def onboarding_page(driver):
    """Run onboarding before each test automatically."""
    try:
        onboarding(driver)  # runs before test
    except:
        pass  # ignore if already onboarded
    yield  # run the test


@pytest.fixture
def logout_after_test(driver):
    """Logout after each test automatically."""
    yield
    try:
        logout(driver)
    except:
        pass  # avoid crashing if already logged out


