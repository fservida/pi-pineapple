from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
    path('network/online', views.check_internet, name="check_online"),
    path('network/interfaces', views.get_interfaces, name="if_list"),
    path('network/wireless/interfaces', views.get_wireless_interfaces, name="wireless_if_list"),
    path('network/wireless/networks', views.get_wireless_networks, name="networks_list"),
    path('network/wireless/hostapd', views.get_hostapd_config, name="hostapd_config"),
    path('network/wireless/hostapd/wps', views.start_wps, name="start_wps"),
    path('network/wireless/hostapd/clients', views.get_hostapd_clients, name="hostapd_clients"),
    # path('network/wireless/hostapd/set', views.set_hostapd_config, name="hostapd_config_set"),
    path('system/services/<str:service_name>/status', views.get_service_status, name="service_status"),
    path('system/services/dhcp/leases', views.get_dhcp_leases, name="dhcp_leases"),
    path('network/mitm/on', views.start_mitm, name="start_mitm"),
    path('network/mitm/off', views.stop_mitm, name="stop_mitm"),
    path('system/services/tcpdump/on', views.start_tcpdump, name="start_tcpdump"),
    path('system/services/tcpdump/off', views.stop_tcpdump, name="stop_tcpdump"),
]
