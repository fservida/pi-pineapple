from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from api import serializers


class Home(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home/home.html"

    def get_context_data(self, **kwargs):
        # Call base implementation
        context = super(Home, self).get_context_data(**kwargs)

        # Get interface informations
        context['interfaces'] = serializers.interfaces()
        context['internet'] = serializers.check_internet()
        context['wireless_interfaces'] = serializers.wireless_interfaces()
        context['hostapd'] = serializers.get_hostapd_config()
        context['services'] = {
            'dhcp': serializers.get_service_status('dnsmasq'),
            'hostapd': serializers.get_service_status('hostapd'),
        }

        return context


class Interfaces(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home/interfaces.html"

    def get_context_data(self, **kwargs):
        # Call base implementation
        context = super(Interfaces, self).get_context_data(**kwargs)

        # Get interface informations
        context['interfaces'] = serializers.interfaces()
        context['wireless_interfaces'] = serializers.wireless_interfaces()

        return context


class Dhcp(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home/dhcp.html"

    def get_context_data(self, **kwargs):
        # Call base implementation
        context = super(Dhcp, self).get_context_data(**kwargs)

        # Get interface informations
        context['services'] = {
            'dhcp': serializers.get_service_status('dnsmasq'),
        }

        context['leases'] = serializers.get_dhcp_leases().get('leases')

        return context


class Hostapd(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home/hostapd.html"

    def get_context_data(self, **kwargs):
        # Call base implementation
        context = super(Hostapd, self).get_context_data(**kwargs)

        # Get interface informations
        context['wireless_interfaces'] = serializers.wireless_interfaces()
        context['hostapd'] = serializers.get_hostapd_config()
        context['services'] = {
            'hostapd': serializers.get_service_status('hostapd'),
        }
        context['clients'] = serializers.get_hostapd_clients()['clients']

        return context


class Monitor(LoginRequiredMixin, TemplateView):
    # TODO
    template_name = "dashboard/home/hostapd.html"

    def get_context_data(self, **kwargs):
        # Call base implementation
        context = super(Monitor, self).get_context_data(**kwargs)

        # Get interface informations
        context['wireless_interfaces'] = serializers.wireless_interfaces()
        context['hostapd'] = serializers.get_hostapd_config()
        context['services'] = {
            'hostapd': serializers.get_service_status('hostapd'),
        }

        return context


class Services(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home/hostapd.html"

    def get_context_data(self, **kwargs):
        # Call base implementation
        context = super(Services, self).get_context_data(**kwargs)

        # Get interface informations
        context['wireless_interfaces'] = serializers.wireless_interfaces()
        context['hostapd'] = serializers.get_hostapd_config()
        context['services'] = {
            'hostapd': serializers.get_service_status('hostapd'),
        }

        return context
