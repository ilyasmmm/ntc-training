def title(title):
    return print('\n', title, '-' * 20)

# ==========================================
# Task 1 - Print Data with a For Loop
# ==========================================

# Step 1-1
# Start a new Python interpreter session, then create the following list of commands:

title('Step 1-1')

commands = ['interface Eth2/1', 'description Configured by Python', 'speed 100', 'duplex full']

print("commands = ['interface Eth2/1', 'description Configured by Python', 'speed 100', 'duplex full']")

# Step 1-2
# Loop through commands and print each element out:

title('Step 1-2')

for command in commands:
    print(command)

# Step 1-3
# Now try this again using a different variable than command. Use for item in commands: instead:

title('Step 1-3')

for item in commands:
    print(item)

# Step 1-4
# Create a list of routers and loop through them printing the following status message for each device:
# Connecting to device | csr1
# But replace csr1 with the correct hostname as you're looping through.

title('Step 1-4')

routers = ['csr1', 'csr2', 'csr3']

for router in routers:
    print("Connecting to device | {}".format(router))

# Step 1-5
# Update the previous loop to ensure each hostname is "uppercase":

title('Step 1-5')

for router in routers:
    print("Connecting to device | {}".format(router.upper()))

# ==========================================
# Task 2 - Loop over a Dictionary
# ==========================================

# Step 2-1
# Create a dictionary that stores information about a network interface that will be configured. The keys will be parameters/features and the values will be the specific commands to send to the device.
# Create this dictionary:

title('Step 2-1')

interface = {}
interface['duplex'] = 'full'
interface['speed'] = '100'
interface['description'] = 'Configured by Python'

print(interface)

# Step 2-2
# Loop through interface, print the keys, values, and then the keys and values together.
# Print the Keys:

title('Step 2-2')

for key in interface.keys():
    print(key)

# Step 2-3
# Print the Values:

title('Step 2-3')

for value in interface.values():
    print(value)

# Step 2-4
# Print the Keys & Values:

title('Step 2-4')

for key, value in interface.items():
    print(key, '--->', value)

for feature, configured_value in interface.items():
    print(feature, '--->', configured_value)

# ==========================================
# Task 3 - Loop over a List of Dictionaries
# ==========================================

# Step 3-1
# Create the VLAN dictionaries

title('Step 3-1')

vlan10 = {'name': 'web', 'id': '10'}
vlan20 = {'name': 'app', 'id': '20'}
vlan30 = {'name': 'db', 'id': '30'}

# Step 3-2
# Create the list of VLANs. Remember, this will be a list of dictionaries since each VLAN is a dictionary.

title('Step 3-2')

vlans = [vlan10, vlan20, vlan30]

# Step 3-3
# Print the vlans variable to see what you just created

title('Step 3-3')

print(vlans)

# Step 3-4
# Pretty print the vlans list

title('Step 3-4')

import json

print(json.dumps(vlans, indent=4))

# Step 3-5
# Loop over vlans and print each element.

title('Step 3-5')

for vlan in vlans:
    print(vlan)

# Step 3-6
# You can verify it by using the type() statement in the for loop.

title('Step 3-6')

for vlan in vlans:
    print(vlan)
    print(type(vlan))

# Step 3-7
# Since you understand the data type of this object now, print the following by using a for loop:

title('Step 3-7')

for vlan in vlans:
    print("vlan {}".format(vlan['id']))
    print(" name {}".format(vlan['name']))


