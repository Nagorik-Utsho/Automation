from logging import exception

from utils.driver_setup import setup_driver
from utils.report_generator import *
from utils.server_status import *
from utils.thrid_party_apps import *
from utils.vpn_activity import *


def split_tunneling_test_execution_steps(driver):
    #1.click on the settings
    click_on(driver, HomePage.settings_page_icon)
    click_on(driver, SettingPage.VPN_setting_menu)
    click_on(driver,VpnSettingsPage.split_tunneling)
    # Find the switch element
    # Find the switch by content-desc

    try :
        toggle = driver.find_element(By.XPATH, '//android.widget.Switch[@content-desc="Chrome"]')

        # Check current state
        current_state = toggle.get_attribute("checked")  # 'true' or 'false'
        print("Current state:", current_state)

        # Toggle only if needed
        if current_state == 'false':  # Switch is OFF
            toggle.click()
    except exception as e :
        print("Button not found")



def main():
    driver=setup_driver()
    time.sleep(1)
    split_tunneling_test_execution_steps(driver)


if __name__ == "__main__":
    main()