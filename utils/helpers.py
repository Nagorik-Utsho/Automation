import time

from .necessary_packages import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, WebDriverException
import time


def click_on(driver, locator, timeout=60):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        element.click()
        time.sleep(0.3)
        #return {"status": "SUCCESS", "message": "Clicked successfully"}

    except TimeoutException as e:
        print("Not found")
         #return {"status": "FAILED", "message": f"Timeout: Element not found → {locator}"}

    except Exception as e:
        print("Not found")
        #return {"status": "FAILED", "message": f"Click failed: {str(e)}"}


def fill_input_field(driver, locator, value, index=0, timeout=30):
    """
    Clicks, clears, and sends keys to an input field at a given index.
    """
    wait = WebDriverWait(driver, timeout)
    fields = wait.until(EC.presence_of_all_elements_located(locator))
    if len(fields) <= index:
        raise Exception(f"Not enough input fields found (index {index})")
    field = fields[index]
    field.click()
    time.sleep(0.5)
    field.clear()
    field.send_keys(value)
    return field





def input_value(driver, locator, data, timeout=30):
    """
    Waits for an input field, clicks, clears, and sends keys.
    Includes exception handling for robustness.
    """
    try:
        wait = WebDriverWait(driver, timeout)
        field = wait.until(EC.presence_of_element_located(locator))

        # Try to click and clear
        try:
            field.click()
            field.clear()
        except ElementNotInteractableException:
            # Fallback for tricky fields (like masked password or Flutter/React Native fields)
            print("⚠️ Element not interactable directly, trying alternative clear method...")
            driver.execute_script("arguments[0].focus();", field)  # focus via JS if supported
            try:
                field.clear()
            except:
                # As last resort, send backspaces
                field.click()
                for _ in range(20):
                    driver.press_keycode(67)  # Android KEYCODE_DEL

        # Send the input
        field.send_keys(data)
        print(f"✅ Input '{data}' sent to field {locator}")
        return True

    except TimeoutException:
        print(f"❌ Timeout: Element {locator} not found after {timeout} seconds")
        return False
    except WebDriverException as e:
        print(f"❌ WebDriverException: {e}")
        return False



def match_element(driver, locator_value,timeout=30) :
    wait=WebDriverWait(driver,timeout)
    field=wait.until(EC.presence_of_element_located((locator_value)))
    text=field.get_attribute('content-desc').strip().lower()
    return text