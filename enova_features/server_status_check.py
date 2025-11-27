import time

from utils.driver_setup import *
from utils.report_generator import *
from utils.server_status import server_status_check
from utils.servers_countries_name_collection import process_server
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





def main():
    driver=setup_driver()
    collecting_servers_name(driver)

if __name__ == "__main__":
    main()