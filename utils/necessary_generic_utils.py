#Go to the server list page
from utils.locators import LocationPage
from utils.necessary_packages import *

#  Scroll in the target scroller and cLick on the selected country
def scroll_and_click_country(driver ,country,max_scrolls_per_direction=2, max_cycles=5):
    """
    Scroll in a ScrollView and click the element if found.
    Returns a dict with status and message.
    """

    possible_scrollviews = [
      LocationPage.scroller_1,
        LocationPage.scroller_2
    ]

    wait = WebDriverWait(driver, 60)
    scrollable = None
    scrollview_xpath = None

    # Try to locate any valid scrollview
    for xpath in possible_scrollviews:
        try:
            scrollable = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
            scrollview_xpath = xpath
            break
        except TimeoutException:
            print(f"⚠️ ScrollView not found with xpath: {xpath}")

    if not scrollable:
        print("❌ No valid ScrollView container found.")
        return {"status": "FAILED", "message": "No valid ScrollView container found"}

    try:
        wait = WebDriverWait(driver, 60)
        scrollable = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, scrollview_xpath)))
    except TimeoutException:
        print("❌ ScrollView container not found.")
        return {"status": "FAILED", "message": "ScrollView container not found"}

    directions = ["down", "up"]

    for cycle in range(max_cycles):
        for direction in directions:
            for attempt in range(max_scrolls_per_direction):
                try:
                    scrollable = driver.find_element(AppiumBy.XPATH, scrollview_xpath)
                    try:
                        element = scrollable.find_element(
                             AppiumBy.XPATH, f".//android.view.View[contains(@content-desc, '{country}')]"
                        )
                        element.click()
                        return {"status": "SUCCESS", "message": f"Element '{country}' clicked successfully"}
                    except NoSuchElementException:
                        driver.execute_script("mobile: scrollGesture", {
                            "elementId": scrollable.id,
                            "direction": direction,
                            "percent": 0.8,
                            "duration":1000
                        })
                        #time.sleep(0.5)
                except StaleElementReferenceException:
                    print("⚠️ ScrollView went stale, retrying...")

    print(f"❌ Element '' not found.")
    return {"status": "FAILED", "message": f"Element '{country}' not found after scrolling"}

#Click on the selected server
def scroll_and_click_server(driver ,server_name,max_scrolls_per_direction=2, max_cycles=5):
    """
    Scroll in a ScrollView and click the element if found.
    Returns a dict with status and message.
    """


    possible_scrollviews = [
      LocationPage.scroller_1,
    LocationPage.scroller_2
    ]

    wait = WebDriverWait(driver, 60)
    scrollable = None
    scrollview_xpath = None

    # Try to locate any valid scrollview
    for xpath in possible_scrollviews:
        try:
            scrollable = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
            scrollview_xpath = xpath
            break
        except TimeoutException:
            print(f"⚠️ ScrollView not found with xpath: {xpath}")

    if not scrollable:
        print("❌ No valid ScrollView container found.")
        return {"status": "FAILED", "message": "No valid ScrollView container found"}

    try:
        wait = WebDriverWait(driver, 60)
        scrollable = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, scrollview_xpath)))
    except TimeoutException:
        print("❌ ScrollView container not found.")
        return {"status": "FAILED", "message": "ScrollView container not found"}

    directions = ["down", "up"]

    for cycle in range(max_cycles):
        for direction in directions:
            for attempt in range(max_scrolls_per_direction):
                try:
                    scrollable = driver.find_element(AppiumBy.XPATH, scrollview_xpath)
                    try:
                        element = scrollable.find_element(
                            AppiumBy.XPATH,
                            f".//android.view.View[contains(@content-desc, '{server_name}')] | .//android.widget.ImageView[contains(@content-desc,'{server_name}')]"
                        )
                        element.click()
                        return {"status": "SUCCESS", "message": f"Element '{server_name}' clicked successfully"}
                    except NoSuchElementException:
                        driver.execute_script("mobile: scrollGesture", {
                            "elementId": scrollable.id,
                            "direction": direction,
                            "percent": 0.7,
                            "duration":1000
                        })
                        #time.sleep(0.5)
                except StaleElementReferenceException:
                    print("⚠️ ScrollView went stale, retrying...")

    print(f"❌ Element '' not found.")
    return {"status": "FAILED", "message": f"Element '{server_name}' not found after scrolling"}


#Collect the countries name

def scroll_and_collect_countries(driver, max_scrolls_per_direction=2, max_cycles=2):
    """
    Scrolls through a ScrollView and collects all element names
    whose XPath matches //android.view.View[contains(@content-desc, "")].
    Returns a dict with status and collected element names.
    """
    print("🔍 Collecting android.view.View elements (with content-desc) from ScrollView...")

    possible_scrollviews = [
        LocationPage.scroller_1,
        LocationPage.scroller_2
    ]

    wait = WebDriverWait(driver, 60)
    scrollable = None
    scrollview_xpath = None

    # Try to locate any valid scrollview
    for xpath in possible_scrollviews:
        try:
            scrollable = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
            scrollview_xpath = xpath
            break
        except TimeoutException:
            print(f"⚠️ ScrollView not found with xpath: {xpath}")

    if not scrollable:
        print("❌ No valid ScrollView container found.")
        return {"status": "FAILED", "message": "No valid ScrollView container found"}

    collected_elements = set()
    directions = ["down", "up"]

    for cycle in range(max_cycles):
        for direction in directions:
            for attempt in range(max_scrolls_per_direction):
                try:
                    scrollable = driver.find_element(AppiumBy.XPATH, scrollview_xpath)

                    # 🔹 Collect elements with the desired XPath shape
                    visible_elements = scrollable.find_elements(
                        AppiumBy.XPATH, ".//android.view.View[contains(@content-desc, '')]"
                    )

                    for el in visible_elements:
                        try:
                            name = el.get_attribute("content-desc")
                            if name and name.strip():
                                collected_elements.add(name.strip())
                        except Exception:
                            pass

                    # 🔹 Scroll further
                    driver.execute_script("mobile: scrollGesture", {
                        "elementId": scrollable.id,
                        "direction": direction,
                        "percent": 0.8,
                        "duration":1000
                    })
                    #time.sleep(0.5)

                except StaleElementReferenceException:
                    print("⚠️ ScrollView went stale, retrying...")

    print(f"✅ Collected {len(collected_elements)} unique android.view.View elements.")
    return {
        "status": "SUCCESS",
        "elements": list(collected_elements)
    }
#Collect the servers name

def scroll_and_collect_all_servers(driver,max_scrolls_per_direction=2, max_cycles=2):
    """
    Scrolls through a ScrollView and collects all element names
    whose XPath matches //android.view.View[contains(@content-desc, "")].
    Returns a dict with status and collected element names.
    """
    print("🔍 Collecting android.view.View elements (with content-desc) from ScrollView...")


    possible_scrollviews = [
      LocationPage.scroller_1,
    LocationPage.scroller_2
    ]

    wait = WebDriverWait(driver, 60)
    scrollable = None
    scrollview_xpath = None

    # Try to locate any valid scrollview
    for xpath in possible_scrollviews:
        try:
            scrollable = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
            scrollview_xpath = xpath
            break
        except TimeoutException:
            print(f"⚠️ ScrollView not found with xpath: {xpath}")

    if not scrollable:
        print("❌ No valid ScrollView container found.")
        return {"status": "FAILED", "message": "No valid ScrollView container found"}

    collected_elements = set()
    directions = ["down", "up"]

    for cycle in range(max_cycles):

        for direction in directions:
            for attempt in range(max_scrolls_per_direction):
                try:
                    scrollable = driver.find_element(AppiumBy.XPATH, scrollview_xpath)

                    # 🔹 Collect elements with the desired XPath shape
                    visible_elements = scrollable.find_elements(
                        AppiumBy.XPATH, ".//android.view.View[contains(@content-desc, '-')] | .//android.widget.ImageView"
                    )

                    for el in visible_elements:
                        try:
                            name = el.get_attribute("content-desc")
                            if name and name.strip():
                                collected_elements.add(name.strip())
                        except Exception:
                            pass

                    # 🔹 Scroll further
                    driver.execute_script("mobile: scrollGesture", {
                        "elementId": scrollable.id,
                        "direction": direction,
                        "percent": 0.6,
                        "duration":1000
                    })
                    #time.sleep(0.5)

                except StaleElementReferenceException:
                    print("⚠️ ScrollView went stale, retrying...")

    print(f"✅ Collected {len(collected_elements)} unique android.view.View elements.")
    return {
        "status": "SUCCESS",
        "elements": list(collected_elements)
    }


