import time

from utils.driver_setup import *
from utils.necessary_adb_commands import reopen_enova
from utils.report_generator import *
from utils.servers_countries_name_collection import match_ip, homepage_info
from utils.vpn_activity import *

countries=set()
servers =set()
def collecting_servers_name(driver):
    global countries, servers
    server_list(driver)
    time.sleep(3)
    countries=collect_countries(driver)
    servers=collect_servers(driver,countries)
    save_to_csv(countries, servers, "collected_countries_servers.csv")

def checking_server_health(driver):
    #1.Read the servers
    countries1, servers1 = load_countries_and_servers("collected_countries_servers.csv")
   # print("Countries: ",countries1)
    #print("Servers: ",servers1)

    # 2.Select the server
    for server in servers1:

        country=detect_country_for_server(server,countries1)
        select_server(driver,server,country)
        connect_server(driver)
        server_info=homepage_info(driver)
        expected_ip=server_info.get("ip_address")
        server_name=server_info.get("Server_name")
        print(f"The expected ip : {expected_ip}")
        match_ip(driver,server_name,expected_ip)
        reopen_enova(driver)
        disconnect_server(driver)
        close_connection_report_popup(driver)





def main():
    driver=setup_driver()
    collecting_servers_name(driver)
    #checking_server_health(driver)


if __name__ == "__main__":
    main()