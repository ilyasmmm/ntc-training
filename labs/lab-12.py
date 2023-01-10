def title(title):
    return print('\n', title, '-' * 20)

# ==========================================
# Task 1 - Use Netmiko in Exec Mode
# ==========================================

# Step 1-3
# Import the netmiko ConnectHandler function and establish an SSH session to the Cloud Services Router device with the following details:

title('Step 1-3')

from netmiko import ConnectHandler

platform = 'cisco_ios'
host = 'csr1'
username = 'ntc'
password = 'ntc123'

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

# Step 1-4
# Issue a dir() on device to see available methods that can be called.

title('Step 1-4')

print(dir(device))

# Step 1-5
# Verify there is an active connection to the device. Verify it is alive.

title('Step 1-5')

print(device.is_alive())

print(help(device.is_alive))

# Step 1-6
# Now we can send a few "show" or "exec" level commands. To do this, use the send_command method.
# Execute the command show version and save the response as a variable

title('Step 1-6')

output = device.send_command('show version')

print(output)

# Step 1-7
# Re-issue the same command using a pipe include to only return the Configuration register

title('Step 1-7')

output = device.send_command('show version | include register')

print(output)

# Step 1-8
# If you want to ensure all config registers are correct, you can use the in containment keyword we covered in the booleans lab like so:

title('Step 1-8')

print('0x2102' in output)

print('0x2142' in output)

# Step 1-9
# Save the configuration using the wr mem command.

title('Step 1-9')

output = device.send_command('wr mem')

print(output)

# Step 1-10
# Let's try checking connectivity to the IP address 10.0.0.15

title('Step 1-10')

output = device.send_command('ping 10.0.0.15')

print(output)

# ==========================================
# Task 2 - Issue Configuration Commands with Netmiko
# ==========================================

# Step 2-1
# Add a new loopback to the device by first creating a list of commands you want to send:

title('Step 2-1')

commands = ['interface Loopback100', 'ip address 10.200.1.20 255.255.255.0']

# Step 2-2
# Use the send_config_set method takes a list as a parameter:

title('Step 2-2')

output = device.send_config_set(commands)

print(output)

# Step 2-3
# You can also use help() to learn more about each method just like you saw with the built-in Python data types.
# For example, here is the help on send_config_set

title('Step 2-3')

print(help(device.send_config_set))

# Step 2-4
# Add two community strings and verify they're configured

title('Step 2-4')

snmp_commands = ['snmp-server community ntclab RO', 'snmp-server community ntcrw RW']

response = device.send_config_set(snmp_commands)

verify = device.send_command('show run | inc snmp-server community')

print(verify)

# Step 2-5
# Let's try to send commands from a file now

title('Step 2-5')

import os

os.system('ls /home/ntc/files/config.txt')

# Step 2-6
# Make sure that you can see the following commands in config.txt

title('Step 2-6')

with open("/home/ntc/files/config.txt", "r") as config:
    data = config.read()

print(data)

# Step 2-7
# Deploy the commands from the config file using the Netmiko method called send_config_from_file

title('Step 2-7')

output = device.send_config_from_file('/home/ntc/files/config.txt')

# Step 2-8
# Verify output has the commands without any errors being received from the device

title('Step 2-8')

print(output)

# ==========================================
# Task 3 - Use Other Built-in Methods
# ==========================================

# Step 3-1
# Enter Config Mode:

title('Step 3-1')

device.config_mode()

# Step 3-2
# By default send_command waits for the device "prompt string" to return to what it was. If you're choosing to send non-global config commands using send_command, the prompt will change. Therefore, you should be aware of send_command_timing

title('Step 3-2')

data = device.config_mode()
data = device.send_command_timing('interface Gigabit3')

# Step 3-3
# You can always view your prompt string'

title('Step 3-3')

print(device.find_prompt())

# Step 3-4
# Exit configuration mode

title('Step 3-4')

device.exit_config_mode()

# Step 3-5
# Disconnect from the device

title('Step 3-5')

device.disconnect()

# Step 3-6
# Validate the SSH connection is no longer active

title('Step 3-6')

print(device.is_alive())

# Step 3-7
# Re-establish connection back to the device

title('Step 3-7')

device.establish_connection()

# Step 3-8
# Finally, disconnect one final time

title('Step 3-8')

device.disconnect()