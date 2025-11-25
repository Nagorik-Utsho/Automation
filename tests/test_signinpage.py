import json
import os

import pytest

from enova_pages.siginpage import *
from utils.vpn_activity import *

# Build the absolute path (optional, but safer)
json_path = r"C:\Users\USER\PycharmProjects\PythonProject\EnovaVpn\Test Data\test_data.json"

# Open and load the JSON file
with open(json_path, 'r', encoding='utf-8') as file:
    test_data = json.load(file)
    print(test_data)

@pytest.mark.parametrize("data", test_data.get("manual_signin", []))
def test_sign_in_email_password(driver, data, onboarding_page,logout_after_test):
    email = data['email']
    password = data['password']
    expected = data['expected']

    result = validate_signin_with_email_password(driver, email, password)
    assert result == expected, f"Login failed for {email}"

@pytest.mark.parametrize("data", test_data.get("valid_activation_code", []))
def test_sign_in_activation_code(driver, data,onboarding_page, logout_after_test):
    code = data['code']
    result = validate_signin_with_activation_code(driver, code)
    logout(driver)
    assert result, f"Activation code login failed: {code}"

def test_sign_in_gmail(driver,onboarding_page, logout_after_test):
    result = validate_signin_with_gmail(driver)
    logout(driver)
    assert result, "Gmail login failed"

def test_sign_in_guest(driver, onboarding_page, logout_after_test):
    result = validate_signin_as_guest(driver)
    logout(driver)
    assert result, "Guest login failed"
