#! /usr/bin/env python

# ==========================================
# Task 1 - Introduction to Functions
# ==========================================

# Step 1-3

def get_vlans():
    return [1, 5, 10, 20]

vlans = get_vlans()

print("\nStep 1-3 ------\n")

print(vlans)

# Step 1-5

def vlan_exists(vlan_id):
    return vlan_id in get_vlans()

print("\nStep 1-5 ------\n")

print(vlan_exists(10))
print(vlan_exists(12))

# ==========================================
# Task 2 - Use Functions to Connect to Network Devices
# ==========================================

from netmiko import ConnectHandler

def ez_cisco(hostname, username, password, show_command):
    print(hostname)
    print(username)
    print(password)
    print(show_command)

def ez_cisco_2(hostname, username, password, show_command):
    platform = "cisco_ios"
    device = ConnectHandler(
        ip=hostname, username=username, password=password, device_type=platform
    )

    output = device.send_command(show_command)
    device.disconnect()

    return output


def ez_cisco_3(hostname, show_command, username="ntc", password="ntc123"):
    platform = "cisco_ios"
    device = ConnectHandler(
        ip=hostname, username=username, password=password, device_type=platform
    )

    output = device.send_command(show_command)
    device.disconnect()

    return output

print("\nStep 2-3 ------\n")

ez_cisco("csr1", "ntc", "ntc123", "show version")

print("\nStep 2-5 ------\n")

response = ez_cisco_2("csr1", "ntc", "ntc123", "show version")

print(response)

print("\nStep 2-5 ------\n")

response = ez_cisco_3("csr1", "show version")
print(response)

response = ez_cisco_3("csr2", "show ip int brief")
print(response)

response = ez_cisco_3("csr3", "show run | inc snmp")
print(response)