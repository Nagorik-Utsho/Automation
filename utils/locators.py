from .necessary_packages import *


class HomePage:
    connecting_button= (By.XPATH,'//android.view.View[contains(@content-desc, "Disconnected")]/android.widget.ImageView[3]')
    disconnecting_button= (By.XPATH,'//android.view.View[contains(@content-desc, "Connected")]/android.widget.ImageView[3]' )
    disconnect_popup=(By.XPATH, '//android.view.View[@content-desc="DISCONNECT"]')
    Location_page=(By.XPATH,'//android.view.View[contains(@content-desc, "Auto")]')

    server_name=(By.XPATH,'//android.widget.ImageView[@content-desc="India - 3\nFree"]')


class CountryDropdown:

    @staticmethod
    def close_dropdown(country_name: str) -> str:
        """
        Returns the XPath for a country dropdown element that matches the given country
        and does not contain a '-' (i.e., only the country name, not servers).
        """
        return f'//android.view.View[contains(@content-desc,"{country_name}") and not(contains(@content-desc, "-"))]'



class LocationPage:
    scroller_1 = (By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.view.View')
    scroller_2 =( By.XPATH,'//android.widget.ScrollView')
    all_location= (By.XPATH,'//android.view.View[@content-desc="All Tab 1 of 3"]')
    premium_collection = (By.XPATH,'//android.view.View[@content-desc="Premium\nTab 2 of 3"]')
    recommended_collection= (By.XPATH,'//android.view.View[@content-desc="Recommended Servers Tab 3 of 3"]')
    click_server_switch=(By.XPATH, '//android.view.View[@content-desc="Switch"]')



class VpnSettingsPage:

    internet_kill_switch_button=(By.XPATH,'//android.view.View[contains(@content-desc,"Internet kill switch")]')
    open_settings_button=(By.XPATH,'//android.view.View[@content-desc="OPEN SETTINGS"]')
    split_tunneling=(By.XPATH,'//android.view.View[contains(@content-desc,"Split tunneling")]' )
    vpn_protocol_page=(By.XPATH,'//android.view.View[@contains(content-desc,"VPN protocol\nPremium"]')


class AndroidPages :
    settings_icon=(By.XPATH ,'//android.widget.ImageView[@content-desc="Settings"]')
    always_on_vpn_button=(By.XPATH,'(//android.widget.Switch[@resource-id="android:id/switch_widget"])[1]')
    block_connection_button=(By.XPATH,'(//android.widget.Switch[@resource-id="android:id/switch_widget"])[2]')
    chrome_browser=(By.XPATH,'//android.widget.Switch[@content-desc="Chrome"]')
    close_split_tunneling_popUp=(By.XPATH,'//android.widget.ImageView')
















