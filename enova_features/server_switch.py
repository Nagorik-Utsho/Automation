import csv

from utils.driver_setup import setup_driver
from utils.necessary_adb_commands import reopen_enova
from utils.report_generator import *
from utils.servers_countries_name_collection import *
from utils.thrid_party_apps import watch_youtube
from utils.vpn_activity import *







def server_switch_check(driver):

    # 1.Server before Server switch
        server, country =pick_servers("collected_countries_servers.csv")
   #  2.Select the server
        select_server(driver, server, country)

    # 3.Connect with the server
        connect_server(driver)
    # 4.Check IP
        server_info = homepage_info(driver)
        expected_ip = server_info.get("ip_address")
        server_name = server_info.get("Server_name")
        match_ip(driver, server_name, expected_ip)
    # 5.Watch youtube videos
        watch_youtube(driver)
    # 6.select server for server
        server, country = pick_servers("collected_countries_servers.csv")
        print(server, country)
        select_server(driver, server, country)
    # 7.Switch server option
        server_switch(driver)
    # 8.Check IP
        server_info = homepage_info(driver)
        expected_ip = server_info.get("ip_address")
        server_name = server_info.get("Server_name")
        match_ip(driver, server_name, expected_ip)
    #9.Reopen Enova
        reopen_enova(driver)
    #10.Disconnect server
        disconnect_server(driver)








def main():

    driver = setup_driver()
    # EXAMPLE
    server_switch_check(driver)







if __name__ == "__main__":
    main()