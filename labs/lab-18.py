#! /usr/bin/env python

from netmiko import ConnectHandler


def connect_to_device(hostname):
    print(f"Connecting to device | {hostname}")
    device = ConnectHandler(
        host=hostname, username="ntc", password="ntc123", device_type="cisco_ios"
    )
    return device


def save_config(device, hostname):
    print(f"Saving configuration | {hostname}")
    device.send_command("wr mem")


def backup_config(device, hostname):
    print(f"Backing up configuration | {hostname}")
    device.send_command("term len 0")
    config = device.send_command("show run")
    return config


def write_to_file(hostname, show_run):
    print(f"Writing config to file | {hostname}\n")
    backup_path = "/home/ntc/labs/python/configs"
    with open(f"{backup_path}/{hostname}.cfg", "w") as config_file:
        config_file.write(show_run)


def main():
    devices = ["csr1", "csr2", "csr3"]

    for device_hostname in devices:
        net_device = connect_to_device(device_hostname)

        save_config(net_device, device_hostname)

        net_config = backup_config(net_device, device_hostname)

        write_to_file(device_hostname, net_config)

        net_device.disconnect()


def test(required_1, required_2, *args, **kwargs):
    print(required_1)
    print(required_2)
    
    if args:
        print(args)

    if kwargs:
        if 'username' in kwargs:
            print('Username = ', kwargs['username'])

        if 'password' in kwargs:
            print('Password = ', kwargs['password'])
        

test(1, 2, 3, 4, 5, username="test", password="test123")