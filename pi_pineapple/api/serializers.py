from api import network, system


def interfaces():
    interfaces_list = network.get_if_list()
    data = {interface: network.get_if_details(interface) for interface in interfaces_list}
    return data


def wireless_interfaces():
    data = {interface: network.get_if_details(interface) for interface in network.get_wireless_interfaces()}
    return data


def wireless_networks(interface="wlan1"):
    data = network.get_wireless_networks(interface)
    return data


def get_service_status(service_name):
    data = {'status': system.get_service_status(service_name)}
    return data


def check_internet():
    data = {'reachable': network.check_internet()}
    return data


def get_hostapd_config():
    data = network.get_hostapd_config()
    return data


def get_hostapd_clients():
    data = {'clients': [network.get_client_details(mac_addr, network.get_arp_table()) for mac_addr in
                        network.get_hostapd_clients()]}
    return data


def set_hostapd_interface(interface):
    config = {
        'interface': interface
    }
    data = {'success': network.set_hostapd_config(config)}
    return data
