def title(title):
    return print('\n', '-' * 5, title, '-' * 5)

# ==========
# Task 1 - Explore Basic List Operations
# ==========

title("STEP 1-1")
# Step 1-1
# Create the following list of MAC addresses and assign them to the variable mac_list
mac_list = ['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33', '44:00:00:00:44:44']

title("STEP 1-2")
# Step 1-2
# Print the value of mac_list
print(mac_list)

title("STEP 1-3")
# Step 1-3
# Using the replace method, update the fourth element in the list so that it uses periods instead of colons
mac_list[3] = mac_list[3].replace(':', '.')

title("STEP 1-4")
# Step 1-4
# Print the new list
print(mac_list)

title("STEP 1-5")
# Step 1-5
# Remove the last element using the pop built-in method.
mac_list.pop()
print(mac_list)

title("STEP 1-6")
# Step 1-6
# Pop the MAC address '00.00.00.00.22.22'. Since this is NOT the last element, you must supply the index value of the value you're looking to pop.
mac_list.pop(1)
print(mac_list)

title("STEP 1-7")
# Step 1-7
# Insert '00.00.00.00.22.22' back into the list at the same position where it was. Use the insert method
mac_list.insert(1, '00.00.00.00.22.22')
print(mac_list)

title("STEP 1-8")
# Step 1-8
# Insert the mac address '22.22.00.00.00.22' as the 3rd element
mac_list.insert(2, '22.22.00.00.00.22')
print(mac_list)

title("STEP 1-9")
# Step 1-9
# Add two more MAC addresses to the list in sequential order using the append method
mac_list.append('55.55.55.55.55.55')
mac_list.append('66.66.66.66.66.66')
print(mac_list)

# ==========
# Task 2 - Build a List of Commands for Network Devices
# ==========

title("STEP 2-1")
# Step 2-1
# Create a list of commands like the following
commands = ['interface Eth1/1', 'description configured by Python', 'shutdown']

title("STEP 2-2")
# Step 2-2
# Convert the list of commands to a string and insert a semi-colon inbetween each command. Use the join method.
cmd_string = ' ; '.join(commands)

title("STEP 2-3")
# Step 2-3
# Print the new variable called cmd_string.
print(cmd_string)

title("STEP 2-4")
# Step 2-4
# Instead of inserting ";", now insert a "\n"
cmd_string_n = '\n'.join(commands)

title("STEP 2-5")
# Step 2-5
# Print the new variable called cmd_string_n
print(cmd_string_n)

title("STEP 2-6")
# Step 2-6
# Perform the same two steps, but this time add a space after the "\n"
cmd_string_n = '\n '.join(commands)
print(cmd_string_n)

title("STEP 2-7")
# Step 2-7
# Continue to try the other built-in methods for lists.
print(dir(list))

# ==========
# Task 3 -  Sort Lists of Similar Objects
# ==========

title("STEP 3-1")
# Step 3-1
# Create a list of Cisco Nexus linecards, noting they are all strings
n7k_linecards = ['N7K-SUP1', 'N7K-M132XP-12', 'N7K-M148GS-11', 'N7K-M148GT-11', 'N7K-F132XP-15', 'N7K-SUP1', 'N7K-M132XP-12', 'N7K-M132XP-12', 'N7K-M148GT-11','N7K-M148GT-11']

title("STEP 3-2")
# Step 3-2
# Verify how many linecards there are either SUP2, SUP1, or M1-32 blades
print(n7k_linecards.count("N7K-SUP2"))
print(n7k_linecards.count("N7K-SUP1"))
print(n7k_linecards.count("N7K-M132XP-12"))

title("STEP 3-3")
# Step 3-3
# You can do the same for verifying how many device types of a given vendor are in your environment
vendors = ["cisco", "cisco", "juniper", "cisco", "arista", "juniper"]
print(vendors.count('cisco'))

title("STEP 3-4")
# Step 3-4
# Sort the vendors list
vendors.sort()
print(vendors)

title("STEP 3-5")
# Step 3-5
# Let's now reverse the list using the optional keyword reverse
vendors.sort(reverse=True)
print(vendors)