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


def get_dhcp_leases():
    # attributes = [
    #     'ip',  # The ip address assigned by this lease as string
    #     'ethernet',  # The mac address of the lease
    #     'hardware',  # The OSI physical layer used to request the lease (usually ethernet)
    #     'start',  # The start time of this lease as DateTime object
    #     'end',  # The time this lease expires as DateTime object or None if this is an infinite lease
    #     'hostname',  # The hostname for this lease if given by the client
    #     'binding_state',  # The binding state as string ('active', 'free', 'abandoned', 'backup')
    #     'valid',  # True if the lease hasn't expired and is not in the future
    #     'active',  # True if the binding state is active
    #     'options',  # List of extra options in the lease file
    #     'sets',
    # ]
    # data = {'leases': [{attribute: getattr(lease, attribute, None) for attribute in attributes} for key, lease in
    #                    network.get_dhcp_leases().items()]}
    data = {'leases': [network.get_dhcp_leases()]}
    return data
