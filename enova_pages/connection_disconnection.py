import time

from utils.driver_setup import setup_driver
from utils.locators import HomePage
from utils.helpers import *

from utils.vpn_activity import *
def main():
    driver=setup_driver()
    time.sleep(5)
    logout(driver)
    # click_on(driver,HomePage.Location_page)
    # click_on(driver,HomePage.server_name)
    # result=click_on(driver,HomePage.connecting_button)
    # print(result)
    # result=click_on(driver,HomePage.disconnecting_button)
    # print(result)
    # result=click_on(driver,HomePage.disconnect_popup)
    # print(result)
    #
    # # click_on(driver,HomePage.disconnecting_button)
    # # click_on(driver,HomePage.disconnect_popup)

if __name__ == "__main__":
    main()