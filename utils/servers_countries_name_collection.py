from utils.necessary_generic_utils import *
from utils.report_generator import *
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
