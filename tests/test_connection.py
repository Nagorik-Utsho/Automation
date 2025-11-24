from utils.helpers import *
from utils.locators import *


def test_connection(driver):

    click_on(driver,HomePage.Location_page)
    click_on(driver,HomePage.server_name)
    result=click_on(driver,HomePage.connecting_button)
    print(result)
    result=click_on(driver,HomePage.disconnecting_button)
    print(result)
    result=click_on(driver,HomePage.disconnect_popup)
    print(result)