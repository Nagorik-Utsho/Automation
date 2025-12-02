from utils.driver_setup import setup_driver
from utils.helpers import click_on
from utils.locators import HomePage, SettingPage, VpnSettingsPage
from utils.necessary_adb_commands import is_internet_reachable
from utils.vpn_activity import *




def kill_switch_execution(driver) :

    click_on(driver, HomePage.settings_page_icon)

    click_on(driver, SettingPage.VPN_setting_menu)

    click_on(driver,VpnSettingsPage.internet_kill_switch_button)

    turn_on_kill_switch(driver)

    click_on(driver,HomePage.home_page_icon)

    disconnect_server(driver)

    is_internet_reachable(driver)

    click_on(driver, HomePage.settings_page_icon)

    click_on(driver, SettingPage.VPN_setting_menu)

    click_on(driver, VpnSettingsPage.internet_kill_switch_button)

    turn_off_kill_switch(driver)

    is_internet_reachable(driver)





def main():
    driver=setup_driver()
    time.sleep(5)
    kill_switch_execution(driver)


if __name__ == "__main__":
    main()