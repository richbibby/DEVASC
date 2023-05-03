import requests
from get_access_token import get_access_token
import json


def add_dnac_device(token):
    url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
    payload = json.dumps({
      "series": "Cisco Catalyst 9000 Series Virtual Switches",
      "managementIpAddress": "10.10.20.200",
      "hostname": "sw5",
      "platformId": "C9KV-UADP-8P",
      "softwareType": "IOS-XE",
      "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
      "role": "CORE"
    })
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }
    response = requests.request("POST", url, headers=headers, verify=False, data=payload)
    if response.ok:
        print(response.text)
    else:
        response.raise_for_status()


if __name__ == '__main__':
    try:
        access_token = get_access_token()
        add_dnac_device(access_token)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
