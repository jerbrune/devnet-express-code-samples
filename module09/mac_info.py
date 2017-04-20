import sys
import requests
requests.packages.urllib3.disable_warnings()
from requests.auth import HTTPBasicAuth
import json
import base64

def main():
  print("********************************************************");
  print("* Cisco CMX MAC Info Python 3 Utility                  *");
  print("* Please provide the input in the following format     *");
  print("*                                                      *");
  print("* macAddress: 00:00:2a:01:00:06                        *");
  print("*                                                      *");
  print("* Control C to exit                                    *");
  print("********************************************************");

  username = 'learning'
  password = 'learning'
  restURL1 = 'https://msesandbox.cisco.com:8081/api/location/v1/historylite/clients/'
  restURL2 = 'https://msesandbox.cisco.com:8081/api/location/v1/compliance/clientcompliance/floor/'

  while True:

       x          = None
       y          = None
       chgOn      = None
       hierarchy  = None
       macAddress = None

       macAddress = input("macAddress: ")

       try:
           response = requests.get(
           url = restURL1 +"/"+ macAddress,
           auth = HTTPBasicAuth(username,password),
           verify=False)

           json_data = response.json()

           x = json_data["Data"][0]["x"]
           y = json_data["Data"][0]["y"]
           chgOn = json_data["Data"][0]["chgOn"]

           response = requests.get(
           url = restURL2 +"/"+ macAddress,
           auth = HTTPBasicAuth(username,password),
           verify=False)

       except requests.exceptions.RequestException as e:
           print(e)

       print("----------------------------------------------------------------")
       print("x, y coordinates: ", x , y)
       print("timestamp (lastLocatedTime): "+ chgOn)
       print("map hierarchy string: ", response.text)
       print("----------------------------------------------------------------")
       print("\nControl C to Exit");

if __name__ == '__main__':
    main()