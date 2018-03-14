from subprocess import call, check_call, check_output, CalledProcessError, run


def start_wps():
    status = call(["hostapd_cli", "wps_pbc"])
    return status == 0


def get_wireless_networks(interface):
    try:
        networks = check_output(["iw", interface, "scan"])
    except CalledProcessError:
        networks = b""
    return networks.decode()


def get_wireless_interfaces():
    try:
        interfaces = check_output(["iwconfig"])
    except CalledProcessError:
        interfaces = b""
    return interfaces.decode()


def get_service_status(service_name):
    try:
        service = check_output(["systemctl", "status", service_name])
    except CalledProcessError:
        service = b""
    return service.decode()


def check_internet():
    targets = ("www.google.com", "8.8.8.8")

    command = " && ".join("ping -c1 {}".format(target) for target in targets)
    internet = call(command, shell=True)

    return internet == 0


def get_hostapd_config():
    try:
        config = check_output(['hostapd_cli', 'get_config'])
    except CalledProcessError:
        config = b""
    return config.decode()


def get_hostapd_clients():
    try:
        clients = check_output(['hostapd_cli', 'all_sta'])
    except CalledProcessError:
        clients = b""

    return clients.decode()


def get_arp_table():
    try:
        arp_table = check_output(['arp', '-a', '-n'])
    except CalledProcessError:
        arp_table = b""
    return arp_table.decode()


def restart_service(service_name):
    try:
        service = check_output(["systemctl", "restart", service_name])
    except CalledProcessError:
        service = b""
    return service.decode()
