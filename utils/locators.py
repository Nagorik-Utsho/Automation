from .necessary_packages import *


class OnBoarding :
    onboard_login_button=(By.XPATH,'//android.view.View[@content-desc="LOGIN"]')




class SigninPage :
    email_input_field=(By.CLASS_NAME, 'android.widget.ImageView')
    password_input_field=(By.XPATH,'//android.widget.EditText')

    signin_button=(By.XPATH, '//android.view.View[@content-desc="SIGN IN"]')

    social_login_button=  (By.XPATH , '//android.widget.ImageView[@content-desc="GOOGLE"]')
    gmail_account=(By.XPATH, '//*[@resource-id="com.google.android.gms:id/account_display_name"]')

    activation_code_button = (By.XPATH,'//android.widget.ImageView[@content-desc="ACTIVATION CODE"]')
    activation_code_input_field=(By.CLASS_NAME,'android.widget.EditText')
    activation_code_continue_button=(By.XPATH,'//android.view.View[@content-desc="CONTINUE"]')

    guest_login_button= (By.XPATH , '//android.view.View[@content-desc="Continue as guest"]')



    """Create new account"""
    create_account_button=()






class HomePage:

    home_page_check = (By.XPATH, '//android.view.View[contains(@content-desc, "Disconnected")]')
    connecting_button= (By.XPATH,'//android.view.View[contains(@content-desc, "Disconnected")]/android.widget.ImageView[3]')
    disconnecting_button= (By.XPATH,'//android.view.View[contains(@content-desc, "Connected")]/android.widget.ImageView[3]' )
    disconnect_popup=(By.XPATH, '//android.view.View[@content-desc="DISCONNECT"]')
    Location_page=(By.XPATH,'//android.view.View[contains(@content-desc, "Auto")]')
    server_name=(By.XPATH,'//android.widget.ImageView[@content-desc="India - 3\nFree"]')

    """ Home page menu icon """
    home_page_icon=(By.XPATH,'//android.widget.Button[@content-desc="Home\nTab 1 of 4"]/android.widget.ImageView[2]')
    premium_page_icon=(By.XPATH,'//android.widget.Button[@content-desc="Premium\nTab 2 of 4"]/android.widget.ImageView[2]')
    support_page_icon=(By.XPATH,'//android.widget.Button[@content-desc="Support\nTab 3 of 4"]/android.widget.ImageView[2]')
    settings_page_icon = (By.XPATH, '//android.widget.Button[@content-desc="Settings\nTab 4 of 4"]')





class SettingPage:
    profile_menu = (By.XPATH,'//android.widget.ImageView[@content-desc="Profile"]')
    VPN_setting_menu=(By.XPATH,'//android.widget.ImageView[@content-desc="VPN settings"]')
    subscription_menu=(By.XPATH,'//android.widget.ImageView[@content-desc="Subscription"]')
    VPN_code_menu=(By.XPATH,'//android.widget.ImageView[@content-desc="VPN code"]')


class ProfilePage:
    back_navigation=(By.XPATH,'//android.view.View[@content-desc="Profile"]/android.widget.ImageView[1]')
    edit_icon=(By.XPATH,'//android.view.View[@content-desc="Profile"]/android.widget.ImageView[2]')
    devices_icon=(By.XPATH,'//android.view.View[@content-desc="Devices"]')
    logout_button=(By.XPATH,'//android.widget.ImageView[@content-desc="Logout"]')

    '''Logout pop-up'''
    logout_2nd_button=(By.XPATH,'//android.view.View[@content-desc="LOGOUT"]')
    logout_cancel_button=(By.XPATH,'//android.view.View[@content-desc="CANCEL"]')


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
    turn_on_vpn_connection=(By.XPATH,'//android.widget.Button[@resource-id="android:id/button1"]')
    chrome_browser=(By.XPATH,'//android.widget.Switch[@content-desc="Chrome"]')
    close_split_tunneling_popUp=(By.XPATH,'//android.widget.ImageView')
















