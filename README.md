# Pi-Pineapple

Setup Ansible on control machine.
eg. /etc/ansible/hosts
```
[RASPI_WIFI]
192.168.10.102  remote_user=pi
```

# Install
```
ansible-playbook pi-pineapple.yaml
ansible-playbook pi-pineapple-django.yaml
ansible-playbook pi-pineapple-tcpdump.yaml
```
