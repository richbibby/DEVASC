from dnacentersdk import api
from prettytable import PrettyTable


def get_dnac_devices():
    dnac = api.DNACenterAPI(base_url='https://sandboxdnac2.cisco.com:443',
                            username='devnetuser', password='Cisco123!', verify=False)

    device_list = dnac.devices.get_device_list()
    return device_list


def print_device_table(device_list):
    table = PrettyTable()
    table.field_names = ["Hostname", "Primary IP", "Platform", "Serial", "Device Type", "Device Role", "Site"]
    for device in device_list:
        hostname = device['hostname'].upper()
        ip_address = device['managementIpAddress']
        software_type = device['softwareType']
        serial_number = device['serialNumber']
        device_type = device['platformId']
        role = device['role']
        site = device['locationName']
        table.add_row([hostname, ip_address, software_type, serial_number, device_type, role, site])
    print(table)


if __name__ == '__main__':
    devices = get_dnac_devices()
    print_device_table(devices)
