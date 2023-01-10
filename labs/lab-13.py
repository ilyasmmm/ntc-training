from netmiko import ConnectHandler

hosts = [ 'csr1', 'csr2' ]

for host in hosts:

    platform = 'cisco_ios'
    username = 'ntc'
    password = 'ntc123'

    print("Connecting to the device", f'[{host}]')
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

    print("Saving the configuration", f'[{host}]')
    device.send_command('write memory')

    print("Backing up configuration", f'[{host}]')
    output = device.send_command('sh run')

    print("Writing configuration to file", f'[{host}]')
    with open(f"./configs/{host}.cfg", "w+") as config:
        config.write(output)

    device.disconnect()



