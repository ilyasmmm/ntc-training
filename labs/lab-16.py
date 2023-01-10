from netmiko import ConnectHandler

hosts = [ 'csr1', 'csr2', 'csr3' ]

for host in hosts:

    platform = 'cisco_ios'
    username = 'ntc'
    password = 'ntc123'

    print(f"Connecting to the device | {host}")
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

    print(f"Saving the configuration | {host}")
    device.send_command('write memory')

    print(f"Backing up configuration | {host}")
    output = device.send_command('sh run')

    print(f"Writing configuration to file | {host}")
    with open(f"./configs/{host}.cfg", "w+") as config:
        config.write(output)

    device.disconnect()