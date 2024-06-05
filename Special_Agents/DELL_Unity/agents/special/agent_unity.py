#!/usr/bin/env python3

import argparse
import requests

### MAIN FUNCTION ###
# ARGUMENTS:
# ipaddr --> IP address of the Unity appliance management interface
# user --> API user name
# password --> API user password
if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument("-a", "--ipaddr", type=ip_address, required=True, help="Host IP address")
     parser.add_argument("-u", "--user", type=str, required=True, help="API user name")
     parser.add_argument("-p", "--password", type=str, required=True, help="API user password")
     args = parser.parse_args()
     
     print("<<<unity_api_status")
