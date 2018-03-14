from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.Home.as_view(), name="homepage"),
    path('dhcp', views.Dhcp.as_view(), name="dhcp"),
    path('hostapd', views.Hostapd.as_view(), name="hostapd"),
    path('monitor', views.Monitor.as_view(), name="monitor"),
    path('services', views.Services.as_view(), name="services"),
    path('interfaces', views.Interfaces.as_view(), name="interfaces"),
]
