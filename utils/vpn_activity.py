from .locators import *
from .helpers import *
from .scroll_utils import *


#Server list page
def server_list(driver):
    """Go to the Server list to check all the servers"""
    #print ("Now in the server list")

    try:
        wait = WebDriverWait(driver, 120)
        server = wait.until(
            EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@content-desc, "Auto")]'))
        )
        server.click()
        time.sleep(2)
        return {"status": "SUCCESS", "message": "Server list opened successfully"}
    except Exception as e:
        return {"status": "FAILED", "message": f"Server list not found: {e}"}

#Connection function
def connect_server(driver):
    """Connect to VPN server"""
    try:

        click_on(driver,HomePage.connecting_button)
        print("Connected with the server ")
        return {"status": "SUCCESS", "message": "Server connected successfully"}
    except Exception as e:
        print("Failed to connect with the server")
        return {"status": "FAILED", "message": f"Failed to connect to server: {e}"}


#Disconnection function
#@retry(max_attempts=3, delay=2)
def disconnect_server(driver):
    """Disconnect the VPN server"""
    try:
        #print("Trying to Disconnect the vpn")
        click_on(driver,HomePage.disconnecting_button)
        click_on(driver,HomePage.disconnect_popup)
        return {"status": "SUCCESS", "message": "Server disconnected successfully"}
    except Exception as e:
        return {"status": "FAILED", "message": f"Failed to disconnect: {e}"}



#Server switching function
#@retry()
def server_switch(driver):
    """Switch the VPN server"""
    try:
        click_on(driver,LocationPage.click_server_switch)
        return {"status": "SUCCESS", "message": "Server switched successfully"}
    except Exception as e:
        return {"status": "FAILED", "message": f"Server switch failed: {e}"}



''' Kill switch turn on '''
def turn_on_kill_switch(driver):
    try:


        print("Now in the wait and click block")

        click_on(driver,VpnSettingsPage.internet_kill_switch_button)
        click_on(driver,VpnSettingsPage.open_settings_button)
        click_on(driver,AndroidPages.settings_icon)
        click_on(driver,AndroidPages.always_on_vpn_button)
        click_on(driver,AndroidPages.block_connection_button)
        click_on(driver,AndroidPages.turn_on_vpn_connection)

        # NEW: Navigate back to app (press back 2-3 times to exit settings fully)
        for _ in range(4):
            driver.back()
            time.sleep(1)  # Brief pause between backs to let transitions settle

        # Optional: Verify we're back in app (log current activity for debugging)
        print(f"Current activity after back nav: {driver.current_activity}")
        return {"status": "SUCCESS", "message": "Kill switch turned on successfully"}
    except Exception as e:
        print(e)
        return {"status": "FAILED", "message": "Failed to turn on the kill switch"}



'''Go back to Home screen after turning on the Kill switch'''
def turn_on_split_tunneling(driver):
    print("Turning on the Split tunneling")
    click_on(driver,VpnSettingsPage.split_tunneling)


#Kill switch turn off function
def turn_off_kill_switch(driver):
    try:

        click_on(driver, VpnSettingsPage.internet_kill_switch_button)
        click_on(driver, VpnSettingsPage.open_settings_button)
        click_on(driver, AndroidPages.settings_icon)
        click_on(driver, AndroidPages.always_on_vpn_button)
        click_on(driver, AndroidPages.block_connection_button)
        # NEW: Navigate back to app (press back 2-3 times to exit settings fully)
        for _ in range(6):
            driver.back()
            time.sleep(1)  # Brief pause between backs to let transitions settle

        # Optional: Verify we're back in app (log current activity for debugging)
        print(f"Current activity after back nav: {driver.current_activity}")
        return {"status": "SUCCESS", "message": "Kill switch turned off  successfully"}

    except Exception as e:
        print("Failed to turn of the kill switch",{e})
        return {"status": "Failed", "message": "Kill switch turning off  failed"}



#Log out function
def logout(driver):

    print("Now in log out Function")
    #Click on the settings menu
    click_on(driver,HomePage.settings_page_icon)
    #click on the profile
    click_on(driver,SettingPage.profile_menu)
    #click on logout button
    click_on(driver,ProfilePage.logout_button)
    #click on 2nd logout button
    click_on(driver,ProfilePage.logout_2nd_button)



def close_connection_report_popup(driver) :
    try:
        click_on(driver,HomePage.close_report_popUp_button)
        print("Successfully closed the pop up message")
    except Exception as e :
        print("Failed to close the pop or Connection report pop up does not exist for this server ")






countries = set()
servers = set()

#collect countries and servers name
def collect_countries(driver) :
    global countries, servers

    result=scroll_and_collect_countries(driver)
    print(countries)

    #Put the countries in the set
    for item in result['elements']:
        if '-' in item :
            servers.add(item)
        else :
            countries.add(item)

    countries.remove("Brazil")
    servers.add("Brazil")
    print(f"Collected countries name :{countries}")

    return countries


def collect_servers(driver , countries) :
    global servers

    for country in countries :
     print(f"Trying to click : {country}")
     scroll_and_click_country(driver, country)
     all_servers =scroll_and_collect_all_servers(driver)

     #Adding the servers name in the set
     for server in all_servers['elements'] :
         servers.add(server)


     print(servers)
     print(f'Total number of server :{len(servers)} ')

    return servers


def detect_country_for_server(server,country_list) :
    """
        Determine which country a server belongs to.
        Returns the matched country or None.
        """
    server = server.strip()
    for country in country_list:
        if server.lower().startswith(country.lower()):
            return country
    return None



#Select any server
def select_server(driver,server ,country):
    #go to server list
    server_list(driver)

    if country:
        scroll_and_click_country(driver, country)
        scroll_and_click_server(driver, server)
    else:
        scroll_and_click_server(driver, server)