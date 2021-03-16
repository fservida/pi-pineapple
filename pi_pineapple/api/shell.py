from subprocess import call, check_call, check_output, CalledProcessError, run
import os

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
    except CalledProcessError as error:
        service = error.output
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


def get_iptables_status():
    try:
        iptables_status = check_output(['iptables', '-L', '-t', 'nat', '-v', '-n'])
    except CalledProcessError:
        iptables_status = b""
    return iptables_status.decode()


def start_mitm():
    status = call(
        "iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080 && iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080",
        shell=True)
    return status == 0


def stop_mitm():
    status = call(
        "iptables -t nat -D PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080 && iptables -t nat -D PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080",
        shell=True)
    return status == 0


def start_service(service_name):
    try:
        service = run(["systemctl", "start", service_name])
    except CalledProcessError:
        return False
    return True


def stop_service(service_name):
    try:
        service = check_output(["systemctl", "stop", service_name])
    except CalledProcessError:
        return False
    return True


def get_file_size(filename):
    try:
        assert os.path.isfile(filename)
        filesize = os.path.getsize(filename)
    except AssertionError:
        return "File Not Found"
    return f"{filesize / 10**9} MB"
