# ==========
# Task 1 - Evaluate Logical Expressions
# ==========

# Step 1-1
# Create a new variable called is_layer3 and assign it the value of True (do not use quotes)
is_layer3 = True

# Step 1-2
# Perform a type check on the variable
print(type(is_layer3))

# Step 1-3
# Create another variable called needs_bgp and assign it the value of False. Then print it out
needs_bgp = False
print(needs_bgp)

# Step 1-4
# Create 3 variables called hostname, vendor and interfaces
hostname = 'nxos-spine1'
vendor = 'cisco'
interfaces = ['Ethernet2/1', 'Ethernet2/2', 'Ethernet2/3']

# Step 1-5
# Use the == operator to evaluate hostname with the nxos-spine2 string and vendor with the cisco string
print(hostname == 'nxos-spine2')
print(vendor == 'cisco')

# Step 1-6
# Use the > (greater than) and != (not equal) operators to evaluate interfaces's list length with the 3 number.
print(len(interfaces) > 3)
print(len(interfaces) != 3)

# Step 1-7
# Note that != says "does not equal", so you can also use this for the hostname check too
print(hostname != 'nxos-spine2')

# Step 1-8
# Now use the in "containment" keyword to evaluate if Ethernet2/4 is a defined interface. You're checking to see if 'Ethernet2/4' is in the interfaces list
print('Ethernet2/4' in interfaces)

# Step 1-9
# You can also see if a sub-string exists in a string
print("Eth" in "Ethernet2/4")
print("eth" in "Ethernet2/4")

# Step 1-10
# It's often good practice to normalize (if possible) before doing the comparison or logic check
print("eth" in "Ethernet2/4".lower())

# Step 1-11
# Use the and operator to evaluate if Ethernet2/2 is a defined interface and vendor equals to cisco
print('Ethernet2/2' in interfaces and vendor == 'cisco')

# When using and, everything must be True for the expression to evaluate to True.
# You can do a quick test to prove this
print(True and True and True and False)
print(True and True and True)

# Step 1-12
# When you use or, only ONE element has to be True for the expression to be True
print(hostname == "nxos-spine2" or hostname == "nxos-spine10")
print(vendor == "cisco" or hostname == "nxos-spine10")

# ==========
# Task 2 - Convert Other Types to Boolean
# ==========

# Step 2-1
# Create a new variable called hostname and assign it the value of "r1"
hostname = "r1"

# Perform a boolean check on this varible using the bool() statement:
print(bool(hostname))

# Step 2-2
# Create a new variable called vendor and assign it the value of a null/empty string
vendor = ""

# Perform the same boolean check
print(bool(vendor))

# Step 2-3
# Create a variable called vendors and assign it the value of ['cisco']. After it's created, do a boolean check
vendors = ['cisco']
print(bool(vendors))

# Step 2-4
# Perform the same excercise by using an empty list as the value
vendors = []
print(bool(vendors))