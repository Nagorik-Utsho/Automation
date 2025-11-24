import time

from .necessary_packages import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def click_on(driver, locator, timeout=60):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        element.click()
        time.sleep(0.3)
        return {"status": "SUCCESS", "message": "Clicked successfully"}

    except TimeoutException as e:
        return {"status": "FAILED", "message": f"Timeout: Element not found → {locator}"}

    except Exception as e:
        return {"status": "FAILED", "message": f"Click failed: {str(e)}"}



