def title(title):
    return print('\n', title, '-' * 20)

# ==========================================
# Task 1 - Nested Dictionary Objects
# ==========================================

# Step 1-1
# Create a variable called facts_list that has the following value

facts_list = [{'customer': 'acme', 'vendor': 'arista', 'hostname': 'APAC1', 'location': 'Sydney', 'device_type': 'switch', 'model': '7050', 'os': 'eos'}, {'customer': 'acme', 'vendor': 'juniper', 'hostname': 'EMEA1', 'location': 'London', 'device_type': 'switch', 'model': 'mx', 'os': 'junos'}, {'customer': 'acme', 'vendor': 'cisco', 'hostname': 'nycr01', 'location': 'new_york', 'device_type': 'switch', 'model': 'catalyst', 'os': 'ios'}]

# Step 1-2
# Pretty print facts_list by using json.dumps

import json

print(json.dumps(facts_list, indent=4))
[
    {
        "customer": "acme",
        "vendor": "arista",
        "hostname": "APAC1",
        "location": "Sydney",
        "device_type": "switch",
        "model": "7050",
        "os": "eos"
    },
    {
        "customer": "acme",
        "vendor": "juniper",
        "hostname": "EMEA1",
        "location": "London",
        "device_type": "switch",
        "model": "mx",
        "os": "junos"
    },
    {
        "customer": "acme",
        "vendor": "cisco",
        "hostname": "nycr01",
        "location": "new_york",
        "device_type": "switch",
        "model": "catalyst",
        "os": "ios"
    }
]

# Step 1-3
# Can you tell this is a list of dictionaries?

# You can tell this visually by seeing the object start with square brackets.
# You can also do a type check!

# Step 1-4
# Do a type check on facts_list

print(type(facts_list))

# Step 1-5
# First, do a length check of facts_list

print(len(facts_list))

# Step 1-6
# Check the data type of the first element in the list

print(type(facts_list[0]))

# OR

first = facts_list[0]

print(type(first))

# Step 1-7
# Our goal is to print out the "location" of the "APAC1" device.
# To do this, you will need to reference the visual print out and see that it's the first element or the element that has an index value of zero.
# First, print out the whole first element

print(facts_list[0])

# Step 1-8
# You can see that a dictionary is returned since the element begins with curly brackets. Let's print out the location

print(facts_list[0]['location'])

# Step 1-9
# Create two new dictionary objects that depict the attributes of neighbor devices and then print them out

neighbor1 = {'neighbor_interface': 'Eth1/2', 'local_interface': 'Eth1/1', 'neighbor': 'R1'}
neighbor2 = {'neighbor_interface': 'Eth1/4', 'local_interface': 'Eth1/2', 'neighbor': 'R2'}

# Step 1-10
# Create a list that is comprised of these neighbors.

neighbors = [neighbor1, neighbor2]

# Step 1-11
# Print neighbors to see the newly formed list

print(neighbors)

# Now pretty print them:

print(json.dumps(neighbors, indent=4))

# Step 1-12
# These neighbors created are the simulated neighbors of "APAC1" which is the device in facts_list[0], i.e. the first element of facts_list.
# Now add the neighbors list as a key/value pair in the dictionary that APAC1 is currently part of. Use the neighbors key.

facts_list[0]['neighbors'] = neighbors

# Step 1-13
# Pretty print the facts_list to see the newly updated dictionary.

print(json.dumps(facts_list, indent=4))

# Step 1-14
# Now print just the hostname of the second neighbor of "APAC1"

print(facts_list[0]['neighbors'][1]['neighbor'])

# ==========================================
# Task 2 - Work with a Nested Facts Dictionary Object
# ==========================================

# Step 2-1
# Start a new Python shell and import the json module

import json

# Step 2-2
# Create a new variable called content and assign the following object like so:

content = {'output': {'ansible_facts': {'fan_info': [{'status': 'Ok', 'model': None, 'hw_ver': '0.0', 'name': 'ChassisFan1'}, {'status': 'None', 'model': None, 'hw_ver': '0.0', 'name': 'ChassisFan2'}, {'status': 'Ok', 'model': '--', 'hw_ver': '--', 'name': 'Fan_in_PS1'}, {'status': 'Failure', 'model': '--', 'hw_ver': '--', 'name': 'Fan_in_PS2'}], 'ansible_net_model': 'NX-OSv Chassis', 'ansible_net_interfaces': {'Ethernet2/13': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/12': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/11': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/10': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/15': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/14': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/1': {'macaddress': '2cc2.604f.feb2', 'state': 'up', 'mode': 'routed', 'duplex': 'full', 'speed': '1000 Mb/s', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}}, 'ansible_net_all_ipv4_addresses': ['10.0.0.71'], 'ansible_net_hostname': 'nxos-spine1', 'hostname': 'nxos-spine1', 'ansible_net_serialnum': 'TM6017D760B', 'interfaces_list': ['mgmt0', 'Ethernet2/1', 'Ethernet2/2', 'Ethernet2/3', 'Ethernet2/4', 'Ethernet2/5', 'Ethernet2/6', 'Ethernet2/7', 'Ethernet2/8', 'Ethernet2/9', 'Ethernet2/10', 'Ethernet2/11', 'Ethernet2/12', 'Ethernet2/13', 'Ethernet2/14', 'Ethernet2/15'], 'ansible_net_gather_subset': ['hardware', 'default', 'interfaces', 'legacy'], 'power_supply_info': [{'status': 'Ok', 'model': 'DS-CAC-845W', 'number': 1}, {'status': 'Absent', 'model': '------------', 'number': 2}], 'platform': 'NX-OSv Chassis', 'ansible_net_version': '7.3(1)D1(1) [build 7.3(1)D1(0.10)]', 'module': [{'status': 'active *', 'model': 'N7K-SUP1', 'type': 'NX-OSv Supervisor Module', 'ports': 0}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}], 'ansible_net_all_ipv6_addresses': [], 'ansible_net_memtotal_mb': 3908, 'ansible_net_filesystems': ['bootflash:'], 'ansible_net_image': 'bootflash:///titanium-d1.7.3.1.D1.0.10.bin', 'os': '7.3(1)D1(1) [build 7.3(1)D1(0.10)]', 'vlan_list': [1]}}}

# Step 2-3
# As you can see it's a very long and complex object. Let's simplify it and pretty print it.

print(json.dumps(content, indent=4))

# Step 2-4
# You can see that content is a dictionary with a single key called output, and multiple levels of nested objects. Take some time to read through the structured data.

# Step 2-5
# After visually seeing it, we'll prove it.
# Print its length using the len() function

print(len(content))

# Step 2-6
# Verify the single key of the dictionary by using the keys method.

print(content.keys())

# Step 2-7
# Let's extract the value of the output key by now saving it into a new variable called output.

output = content['output']

print(type(output))

print(output.keys())

# Step 2-8
# Pretty print the new variable called output

print(json.dumps(output, indent=4))

# Step 2-9
# This is again a dictionary of one root key, ansible_facts, whose value is still a dictionary, which you saw in Step 8 by printing all keys of output. You could verify it with len() too.
# Repeat the step by step process as necessary in order to print just the value of the fan_info key

print(json.dumps(output['ansible_facts']['fan_info'], indent=4))

# Step 2-10
# This time the value is not a dictionary but a list of four dictionaries. You can see that it's a list visually because the value starts with a [ and ends with a ].
# But you can also verify using the following type function statement

print(type(output['ansible_facts']['fan_info']))

# Step 2-11
# Print the second dictionary in this list.

print(json.dumps(output['ansible_facts']['fan_info'][1], indent=4))

# Step 2-12
# Store the value of the name key ("ChassisFan2") into a new variable called fan_name.
# Finally, print the variable called fan_name.

fan_name = output['ansible_facts']['fan_info'][1]['name']

print(fan_name)

# Step 2-13 - Challenge!
# Now print the list of all interfaces found under the ansible_net_interfaces key. Only print the interface names - do not print their values.
# Use a dictionary built-in method to accomplish this.

interfaces = output['ansible_facts']['ansible_net_interfaces']
print(interfaces.keys())

# Step 2-14 - Challenge!
# Print output again.
# Take a deeper look at its format and focus on the ansible_net_interfaces key. This is another nested dictionary.
# Store the "Ethernet2/11" MAC address value in a variable called mac and print it.

mac = output['ansible_facts']['ansible_net_interfaces']['Ethernet2/11']['macaddress']
print(mac)

# ==========================================
# Task 3 - Handle VLAN Objects
# ==========================================

# Step 3-1
# Create a new variable called vlans that contains the following object

vlans = {
    "output": {
        "proposed": {
            "name": "NTC"
        },
        "existing_vlans_list": [
            "1"
        ],
        "end_state_vlans_list": [
            "1",
            "100"
        ],
        "existing": {},
        "updates": [
            "vlan 100",
            "name NTC",
            "exit"
        ],
        "end_state": {
            "vlan_state": "active",
            "mapped_vni": "",
            "admin_state": "up",
            "name": "NTC",
            "vlan_id": "100"
        },
        "proposed_vlans_list": [
            "100"
        ]
    }
}

# Step 3-2
# Search for existing_vlans_list and proposed_vlans_list keys and store their values into existing_vlans and proposed_vlans.

existing_vlans = vlans['output']['existing_vlans_list']
proposed_vlans = vlans['output']['proposed_vlans_list']

# Step 3-3
# Print both existing_vlans and proposed_vlans.

print(existing_vlans)
print(proposed_vlans)

# Step 3-4
# Create a new variable called end_state_vlans and assign it the sum of existing_vlans and proposed_vlans and print the result.

end_state_vlans = existing_vlans + proposed_vlans
print(end_state_vlans)


# Step 3-5
# Verify that end_state_vlans is equal to the end_state_vlans_list inner key from vlans dictionary.

end_state_vlans == vlans['output']['end_state_vlans_list']
print(end_state_vlans)

# Step 3-6
# You'll also find a key called updates in this VLAN object.
# Print exactly and only the last command found in the updates list.

print(vlans['output']['updates'][2])

# You could have also done this without knowing how many items are in the list:

print(vlans['output']['updates'][-1])