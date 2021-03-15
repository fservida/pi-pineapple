import re

from api import shell


def get_service_status(service_name):
    service = shell.get_service_status(service_name)

    status_re = r"Active:(?P<status>.*)\("
    try:
        status = re.search(status_re, service).group('status').strip()
    except AttributeError:
        status = "unknown"
    return status, service
