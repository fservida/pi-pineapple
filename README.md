# Pi-Pineapple
Setup an hotspot with MITM functionalities on a raspberry pi, with a web interface to control status and enable/disable MITM services.

Sets up a LAN subnet with 10.20.30.0/24 address range.

# Requirements
- Raspberry-Pi with Raspbian GNU/Linux 10 (buster).
- Machine with ansible installed to configure the RPi

Setup Ansible on control machine.
```
pip3 install ansible
```
Setup ansible Host file
eg. /etc/ansible/hosts
```
[RASPI_WIFI]
192.168.10.102  remote_user=pi
```
# Configure
Edit variables in pi-pineapple.yaml to match desired hotspot settings

# Install
```
ansible-playbook pi-pineapple.yaml
ansible-playbook pi-pineapple-django.yaml
ansible-playbook pi-pineapple-tcpdump.yaml
```
- Connect to hotspot wifi
```
ssh pi@10.20.30.1
cd /opt/pi-pineapple
python3 manage.py createsuperuser
```

# Manage
- Connect to hotspot wifi
- Open 10.20.30.1:8000 in your browser
- Login with previously created credentials