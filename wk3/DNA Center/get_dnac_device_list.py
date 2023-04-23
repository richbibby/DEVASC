import requests
from prettytable import PrettyTable


def get_access_token():
    url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
    username = "devnetuser"
    password = "Cisco123!"

    response = requests.post(url, auth=(username, password), verify=False)
    if response.ok:
        token = response.json()['Token']
        return token
    else:
        response.raise_for_status()


def get_dnac_devices(token):
    url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }

    response = requests.get(url, headers=headers, verify=False)
    if response.ok:
        device_list = response.json()['response']
        return device_list
    else:
        response.raise_for_status()


def print_device_table(device_list):
    table = PrettyTable()
    table.field_names = ["Hostname", "Primary IP", "Platform", "Serial Number", "Device Type", "Device Role"]
    for device in device_list:
        hostname = device['hostname']
        ip_address = device['managementIpAddress']
        software_type = device['softwareType']
        serial_number = device['serialNumber']
        device_type = device['type']
        role = device['role']
        table.add_row([hostname, ip_address, software_type, serial_number, device_type, role])
    print(table)


if __name__ == '__main__':
    try:
        access_token = get_access_token()
        devices = get_dnac_devices(access_token)
        print_device_table(devices)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
