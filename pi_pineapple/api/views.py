from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, Http404
from django.template.response import TemplateResponse
import os

from api import shell, serializers


@login_required
def start_wps(request):
    if request.method == 'GET':
        if shell.start_wps():
            data = {'status': 'success'}
            return JsonResponse(data)
        else:
            data = {
                'error_message': 'Error while enabling WPS',
            }
            return JsonResponse(data, status=500)
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)

@login_required
def start_mitm(request):
    if request.method == 'GET':
        if shell.start_mitm():
            data = {'status': 'success'}
            return JsonResponse(data)
        else:
            data = {
                'error_message': 'Error while starting MITM',
            }
            return JsonResponse(data, status=500)
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def stop_mitm(request):
    if request.method == 'GET':
        if shell.stop_mitm():
            data = {'status': 'success'}
            return JsonResponse(data)
        else:
            data = {
                'error_message': 'Error while stopping MITM',
            }
            return JsonResponse(data, status=500)
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


# TODO change functions to accept argument and generalize to all services
@login_required
def start_tcpdump(request):
    if request.method == 'GET':
        if shell.start_service('tcpdump'):
            data = {'status': 'success'}
            return JsonResponse(data)
        else:
            data = {
                'error_message': 'Error while starting tcpdump',
            }
            return JsonResponse(data, status=500)
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def stop_tcpdump(request):
    if request.method == 'GET':
        if shell.stop_service('tcpdump'):
            data = {'status': 'success'}
            return JsonResponse(data)
        else:
            data = {
                'error_message': 'Error while stopping tcpdump',
            }
            return JsonResponse(data, status=500)
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def get_interfaces(request):
    if request.method == 'GET':
        return JsonResponse(serializers.interfaces())
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def get_wireless_interfaces(request):
    if request.method == 'GET':
        return JsonResponse(serializers.wireless_interfaces())
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def get_wireless_networks(request):
    if request.method == 'GET':
        data = serializers.wireless_networks()
        if request.GET.get('format') == 'html':
            return TemplateResponse(request, "api/wireless_networks.html", {'networks': data})
        return JsonResponse(data)

    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def get_service_status(request, service_name):

    allowed_services = ('isc-dhcp-server', 'hostapd')

    if request.method == 'GET':
        if service_name in allowed_services:
            data = serializers.get_service_status(service_name)
            return JsonResponse(data)
        else:
            data = {
                'error_message': 'Unallowed service',
            }
            return JsonResponse(data, status=400)
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def check_internet(request):
    if request.method == 'GET':
        return JsonResponse(serializers.check_internet())
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def get_hostapd_config(request):
    if request.method == 'GET':
        return JsonResponse(serializers.get_hostapd_config())
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)

@login_required
def set_hostapd_config(request):
    if request.method == 'GET':
        for key, value in request.GET.items():
            if key == 'interface':
                return JsonResponse(serializers.set_hostapd_interface(value))

        data = {
            'error_message': 'Unsupported key',
        }
        return JsonResponse(data, status=400)

    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def get_hostapd_clients(request):
    if request.method == 'GET':
        return JsonResponse(serializers.get_hostapd_clients())
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)


@login_required
def get_dhcp_leases(request):
    if request.method == 'GET':
        return JsonResponse(serializers.get_dhcp_leases())
    else:
        data = {
            'error_message': 'Unsupported access method',
        }
        return JsonResponse(data, status=400)

@login_required
def download_file(request, file):
    paths = {
        'pcap': '/var/tcpdump/tcpdump.pcap',
        'sslkeylog': '/var/mitmproxy/sslkeylogfile.txt',
    }
    file_path = paths.get(file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
