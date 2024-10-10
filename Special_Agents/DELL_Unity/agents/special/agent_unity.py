#!/usr/bin/env python3

import argparse
import requests
from ipaddress import ip_address

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

     # "X-EMC-REST-CLIENT": "true" is mandatory
     headers = {
          "Accept": "application/json",
          "Content-type": "application/json",
          "X-EMC-REST-CLIENT": "true"
     }

     authentication = (args.user, args.password)

     baseurl = "https://{}".format(args.ipaddr)
     query = "/api/types/disk/instances"
     parameters = "?compact=true"
     url = baseurl + query + parameters

     requests.packages.urllib3.disable_warnings()
     req = requests.get(url, headers=headers, auth=authentication, verify=False)

     print("<<<unity_api_status>>>")
     print(req.status_code)
     print(req.json()['entries'])

