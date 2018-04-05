import netifaces as ni
import re
from netifaces import AF_INET, AF_LINK

from isc_dhcp_leases import IscDhcpLeases
from manuf import manuf

from api import shell


def get_if_list():
    return ni.interfaces()


def get_if_details(interface):
    try:
        mac_addr = {
            "mac_addr": ni.ifaddresses(interface)[AF_LINK][0]['addr']
        }
    except KeyError:
        mac_addr = {}

    try:
        ip_details = ni.ifaddresses(interface)[AF_INET][0]
    except KeyError:
        ip_details = {}

    details = dict(ip_details, **mac_addr)
    return details


def get_wireless_networks(interface):
    """
    Get Available networks list
    :return:
    """

    split_re = re.compile(r"^BSS", re.MULTILINE)
    bssid_re = r"^(?P<bssid>(?:[\da-f]{2}[:-]){5}[\da-f]{2})"
    essid_re = r"SSID: (?P<essid>.*)"

    networks = shell.get_wireless_networks(interface)
    networks = [network.strip() for network in re.split(split_re, networks) if network != ""] if networks else []
    networks = {re.search(essid_re, network).group("essid"): re.search(bssid_re, network).group("bssid") for network in
                networks}

    return networks


def get_wireless_interfaces():
    """
    Get Wireless Interfaces on system
    :return:
    """

    interfaces_re = re.compile(r"^(.*)IEEE 802\.11", re.MULTILINE)
    interfaces = [interface.strip() for interface in re.findall(interfaces_re, shell.get_wireless_interfaces())]

    return interfaces


def check_internet():
    internet = shell.check_internet()

    return internet


def get_hostapd_config():
    """
    Gets config from hostapd and parses into dict
    :return:
    """

    regexes = re.compile(
        r"Selected interface '(?P<interface>.*)'\nbssid=(?P<bssid>.*)\nssid=(?P<essid>.*)\nwps_state=(?P<wpd_status>.*)\npassphrase=(?P<psk>.*)")

    try:
        config = re.search(regexes, shell.get_hostapd_config()).groupdict()
    except AttributeError:
        config = {}

    return config


def set_hostapd_config(new_config):
    """
    Updates hostapd config with the new values
    :param new_config:
    :type new_config: dict
    :return:
    """

    with open("/etc/hostapd/hostapd.conf", "r") as f:
        config = f.read()

    for conf_key, value in new_config.items():
        regex = re.compile(r"^(" + conf_key + r"=)(.*)$", re.MULTILINE)
        config = re.sub(regex, r"\1" + value, config)

    with open("/etc/hostapd/hostapd.conf", "w") as f:
        f.write(config)

    shell.restart_service('hostapd')
    return 1


def get_hostapd_clients():
    bssid_re = re.compile(r"^((?:[a-f\d]{2}:){5}[a-f\d]{2})$", re.MULTILINE)

    clients = re.findall(bssid_re, shell.get_hostapd_clients())

    return clients


def get_arp_table():
    ip_mac_re = re.compile(r"(?P<ip>(?:[\d]{1,3}\.){3}[\d]{1,3}).*at.*(?P<mac>(?:[a-f\d]{2}:){5}[a-f\d]{2})")

    arp_table = {line.groupdict()['mac'].lower(): line.groupdict()['ip'] for line in
                 [re.search(ip_mac_re, line) for line in filter(lambda x: x, shell.get_arp_table().split("\n"))] if
                 line}

    return arp_table


def get_client_details(mac_address, arp_table=None):
    arp_table = arp_table if arp_table is not None else get_arp_table()
    client_details = {
        'mac_address': mac_address,
        'ip_address': arp_table[mac_address],
        'manufacturer': manuf.MacParser().get_manuf(mac_address),
    }

    return client_details


def get_dhcp_leases():
    leases_file = "/var/lib/dhcp/dhcpd.leases"

    leases = IscDhcpLeases(leases_file)

    return leases.get_current()
