# tests/conftest.py
import pytest
import subprocess
import os
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

# ------------------------------------------------------------------
# Helper: Detect real device OR use emulator in CI
# ------------------------------------------------------------------
def get_android_device_info():
    """
    Returns (device_udid, android_version)
    - On local machine: uses connected real device
    - In CI/Docker: uses 'emulator-5554' (standard Appium Docker name)
    """
    # If running in CI (GitHub Actions, GitLab, etc.), use emulator
    if os.getenv("CI") or os.getenv("GITHUB_ACTIONS"):
        print("Running in CI → using Android emulator (emulator-5554)")
        return "emulator-5554", "11"  # You can change version if needed

    # Local development: detect real connected device
    print("Detecting real connected Android device...")
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, timeout=10)
    lines = result.stdout.strip().split('\n')[1:]

    devices = []
    for line in lines:
        if '\tdevice' in line:
            udid = line.split('\t')[0]
            devices.append(udid)

    if not devices:
        raise Exception("No Android device/emulator found! Connect a device or start emulator.")

    device_udid = devices[0]
    print(f"Found real device: {device_udid}")

    # Get Android version
    version_result = subprocess.run(
        ['adb', '-s', device_udid, 'shell', 'getprop', 'ro.build.version.release'],
        capture_output=True, text=True, timeout=10
    )
    android_version = version_result.stdout.strip() or "11"
    print(f"Android version: {android_version}")

    return device_udid, android_version


# ------------------------------------------------------------------
# Pytest Fixture: driver (session scope = one driver per test run)
# ------------------------------------------------------------------
@pytest.fixture(scope="session")
def driver():
    device_udid, android_version = get_android_device_info()

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = android_version
    options.device_name = device_udid
    options.automation_name = "UiAutomator2"

    # App settings - CHANGE THESE TO YOUR APP!
    options.app_package = "com.dailycalai.app"
    options.app_activity = "com.dailycalai.app.MainActivity"

    # Recommended options
    options.no_reset = False                  # Set False in CI for clean state
    options.full_reset = os.getenv("CI")      # Full reset only in CI
    options.new_command_timeout = 600
    options.auto_grant_permissions = True
    options.dont_stop_app_on_reset = True

    # Appium server URL
    appium_url = os.getenv("APPIUM_HOST", "http://127.0.0.1:4723")

    print(f"Connecting to Appium at {appium_url}")
    print(f"Target device: {device_udid} (Android {android_version})")

    driver = webdriver.Remote(appium_url + "/wd/hub", options=options)
    driver.implicitly_wait(10)

    yield driver

    # Teardown: quit driver
    print("Quitting Appium driver...")
    driver.quit()


# ------------------------------------------------------------------
# Optional: Health check fixture to wait for device ready
# ------------------------------------------------------------------
@pytest.fixture(autouse=True)
def wait_for_device_ready(driver):
    """Wait a moment for device to be fully ready after session start"""
    time.sleep(5)
    # You can add extra checks here if needed