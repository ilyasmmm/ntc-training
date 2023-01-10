def title(title):
    return print('\n', title, '-' * 20)

import json

# ==========================================
# Task 1 - Introduction to the IF Statement
# ==========================================

# Step 1-1
# Each of the expressions can easily be used in an if statement. Start a new Python interactive interpreter in a terminal session.
# Try the following examples that map what was done previously:

title('Step 1-1')

hostname = "nxos-spine1"
if hostname == "nxos-spine1":
    print("The hostname is correct.")

# Step 1-2
# Another example, testing membership of a list of results that might come from gathering data about your network devices.

title('Step 1-2')

platforms = ['nexus', 'catalyst', 'asa', 'csr', 'aci']
if 'catalyst' in platforms:
    print("Catalyst has been found in the network.")

# Step 1-3
# Create a variable called supported_platforms and assign it the value of ['nexus', 'catalyst'].
# Determine which of the platforms are supported platforms using a combination of conditional logic and a for loop

title('Step 1-3')

supported_platforms = ['nexus', 'catalyst']

for platform in platforms:
    if platform in supported_platforms:
        print("Platform {}  -- SUPPORTED".format(platform))

# Step 1-4
# Add an else statement to the previous example printing an equivalent statement so we can see even the invalid platforms.

title('Step 1-4')

for platform in platforms:
    if platform in supported_platforms:
        print("Platform {}  -- SUPPORTED".format(platform))
    else:
        print("Platform {}  -- NOT SUPPORTED".format(platform))

# Step 1-5
# Create the following list of dictionaries

title('Step 1-5')

vlans = [{'name': 'web', 'id': 10}, {'name': 'app', 'id': 20}, {'name': 'db', 'id': 30}]

print(vlans)

# Step 1-6
# Print ONLY the VLAN name for VLAN 20. Assume there are 100s of VLANs in this list and you don't know the VLANs index value.

title('Step 1-6')

for item in vlans:
    if item['id'] == 20:
        print("VLAN NAME: {}".format(item['name']))

# Step 1-7
# Generate and print all required Cisco IOS commands to configure the list of desired VLANs

title('Step 1-7')

for item in vlans:
    vlan_id = item['id']
    name = item['name']
    print("vlan {}".format(vlan_id))
    print(" name {}".format(name))

# Step 1-8
# Remove the VLAN name for VLAN 20.

title('Step 1-8')

vlans[1].pop('name')

print("vlans[1].pop('name')")

# Step 1-9
# Repeat Step 6.

title('Step 1-9')

for item in vlans:
    if item['id'] == 20:
        try:
            print("VLAN NAME: {}".format(item['name']))
        except Exception as e:
            print(e)

# Step 1-10
# When you use the [] notation it assumes the key is going to be there and if it's not (like for VLAN 20), a KeyError is raised.
# However, we did cover in the booleans section AND the dictionary section a method we can use to overcome this.
# ALWAYS, if a dictionary key may not exist, do NOT use the notation like dict['key']. Instead, you should use dict.get('key')
# Once you extract a value using get, you can perform a conditional check on it to see if it has a value assigned. For reference scroll up and look at the examples before Step 1.

title('Step 1-10')

for item in vlans:
    vlan_id = item['id']
    name = item.get('name')
    print("vlan {}".format(vlan_id))
    if name:
        print(" name {}".format(name))

# Step 1-11
# Create the variable called devices as such:

title('Step 1-11')

devices = [{'platform': 'nexus', 'hostname': 'nycr01'}, {'platform': 'catalyst', 'hostname': 'nycsw02'}, {'platform': 'mx', 'hostname': 'nycr03'}, {'platform': 'srx', 'hostname': 'nycfw01'}, {'platform': 'asa', 'hostname': 'nycfw02'}]

print(json.dumps(devices, indent=4))

# Step 1-12
# Loop through devices and print the vendor of each device. Make sure the code also prints out "Unknown Vendor" if it is an unknown vendor - for this example, treat the ASA as "unknown".
# Make sure to use the elif statement in this example

title('Step 1-12')

for item in devices:
    platform = item.get('platform')
    if platform == "nexus":
        print("Vendor is Cisco")
    elif platform == "catalyst":
        print("Vendor is Cisco")
    elif platform == "aci":
        print("Vendor is Cisco")
    elif platform == "srx" or platform == "mx":
        print("Vendor is Juniper")
    else:
        print("Unknown Vendor")

# Step 1-13
# There is another way too if we pre-build a known platform list per vendor.

title('Step 1-13')

cisco_platforms = ['catalyst', 'nexus', 'aci']
juniper_platforms = ['mx', 'srx']

for item in devices:
    platform = item.get('platform')
    if platform in cisco_platforms:
        print("Vendor is Cisco")
    elif platform in juniper_platforms:
        print("Vendor is Juniper")
    else:
        print("Unknown Vendor")

