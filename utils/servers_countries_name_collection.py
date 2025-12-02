import time

from utils.report_generator import *
from utils.scroll_utils import *
from utils.thrid_party_apps import get_ip_from_app
from utils.vpn_activity import connect_server, server_list

countries = set()
servers = set()

def collect_countries_servers(driver):

    result=scroll_and_collect_countries(driver)
    print(result)

    for item in result['elements']:
        if '-' in item :
            servers.add(item)
        else :
            countries.add(item)

    countries.remove("Brazil")
    servers.add("Brazil")
    print(f"Collected countries name :{countries}")

    for country in countries :
        #xpath = CountryDropdown.close_dropdown(country)
        print(f"Trying  to click:{country}")
        scroll_and_click_country(driver,country)

        all_servers=scroll_and_collect_all_servers(driver)

        for premium_server in all_servers['elements'] :
            servers.add(premium_server)

        # Step 2: Wait for it and click
        #wait_and_click(driver, xpath)
        #time.sleep(.2)

    print(servers)
    print(f'Total number of server :{len(servers)} ')



def collecting_servers_name(driver):

    server_list(driver)
    time.sleep(3)
    collect_countries_servers(driver)
    save_to_csv(countries, servers, "collected_countries_servers.csv")



#Identify which country a server belongs to
def find_server_country(server, countries):
    server = server.strip()

    for country in countries:
        if server.lower().startswith(country.lower()):
            return country

    return None  # No matching country



#Navigate to the server
def navigate_to_server(driver, server, country):
    server_list(driver)

    if country:
        print(f"🌍 Server '{server}' belongs to '{country}'")
        scroll_and_click_country(driver, country)
        scroll_and_click_server(driver, server)
    else:
        print(f"⚡ Server '{server}' not tied to a country — searching directly")
        scroll_and_click_server(driver, server)


def process_server(driver, server, countries):
    country = find_server_country(server, countries)
    navigate_to_server(driver, server, country)
    connect_server(driver)






def match_ip(driver,server_name,expected_ip) :

    result=get_ip_from_app(driver)

    actual_ip=result.get("ip")
    print(f"Captured IP from the APP : {actual_ip}")
    if expected_ip == actual_ip :

        print(f"✔️ IP matched for {server_name} " )
        return {"status": "SUCCESS", "message": " ✔️ IP matched  "}

    else :
        print(f"❌ IP not matched for {server_name}")
        return {" status": "FAILED", "message": " ❌ IP not matched"}






#From the home page after connection collects the server name , ip and other information
def homepage_info(driver):
    wait = WebDriverWait(driver, 5)
    server_name = ''
    ip_address = ''
    try:
        get_serverinfo = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, f'//android.view.View[contains(@content-desc,"Connected")]')
        ))

        for elem in get_serverinfo:
            content_desc = elem.get_attribute("content-desc")
            if content_desc:
                lines = content_desc.split("\n")
                if len(lines) >= 7:
                    server_name = lines[1]
                    ip_address = lines[2]
                    downloaded = lines[4]
                    uploaded = lines[6]
        return {"Server_name": server_name, "ip_address": ip_address}
    except Exception as e:
        print("Failed to gather information from the home page")

    return ip_address



