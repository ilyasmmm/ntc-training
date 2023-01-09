# ==========
# Task 1 - Explore Dictionary Syntax
# ==========

# Step 1-1
# Create a variable called facts and assign it the value of {} that will make it an empty dictionary
facts = {}

# Step 1-2
# Perform a type check on facts to prove it's a dictionary
print(type(facts))

# Step 1-3
# Add a single key-value pair to the facts dictionary. The key should be 'vendor' and the value should be 'cisco'
facts['vendor'] = 'cisco'

# Step 1-4
# Print the dictionary after adding the key-value pair:
print(facts)

# Step 1-5
# Perform a len() check on facts
print(len(facts))

# Step 1-6
# Add a few more key-value pairs as shown below and when done, print the updated facts dictionary
facts['os'] = 'nxos'
facts['version'] = '7.1'
facts['platform'] = 'nexus'
print(facts)

# Step 1-7
# Update the version from "7.1" to "7.3" and print the dictionary to verify it
facts['version'] = "7.3"
print(facts)

# Step 1-8
# You can also create a dictionary using the same notation you see when you print it. In the first few steps, you gradually added key-value pairs. However, you could just assign a new dictionary a value when it's created too
facts_2 = {'os': 'ios', 'version': '16.6', 'vendor': 'cisco', 'platform': 'catalyst'}

# Step 1-9
# Another option is to use the built-in dict() function when creating dictionaries
facts_3 = dict(hostname='APAC1', vendor='arista', location='Sydney', model='7050')
print(facts_3)

# Step 1-10
# Using this same syntax, you can also create an empty dictionary
facts_4 = dict()
print(facts_4)

# ==========
# Task 2 - Update and Modify Dictionary Contents
# ==========

# Step 2-1
# Review the built-in methods for dictionaries using the dir() function on facts
print(dir(facts))

# Step 2-2
# Print the keys for facts
print(facts.keys())

# Step 2-3
# Print the values for facts
print(facts.values())

# Step 2-4
# Now print the keys and the values for facts_2
print(facts_2.keys())
print(facts_2.values())

# Step 2-5
# Print the value for hostname in facts_3
print(facts_3['hostname'])

# Step 2-6
# Print the value for the key called os in facts
print(facts['os'])

# Step 2-7
# Try to print the value for a key called os_version in facts
try:
    print(facts['os_version'])
except Exception as e:
    print(e)

# Step 2-8
# Now use the get method to try and return the value assigned to the os_version key
print(facts.get('os_version'))

# Step 2-9
# Not only is get cleaner, but you can return a designated value if the desired key doesn't exist
print(facts.get('os_version', 'ERROR'))

# Step 2-10
# Repeat the same step, but do not return "ERROR"
os_ver = facts.get('os_version')
print(os_ver)

# Step 2-11
# Remove the hostname key-value pair from facts_3 using the pop method.
print(facts_3)
facts_3.pop('hostname')
print(facts_3)

# Step 2-12
# Update the hostname of facts_3 to be nycr01
facts_3['hostname'] = 'nycr01'
print(facts_3)

# Step 2-13
# Create a new dictionary called static_facts. It should have two key value pairs
static_facts = {'customer': 'acme', 'device_type': 'switch'}

# Step 2-14
# The facts in the static_facts dictionary are pertinent for all 3 other devices that already have their own facts dictionaries: facts, facts_2, facts_3
facts.update(static_facts)
facts_2.update(static_facts)
facts_3.update(static_facts)

print(facts)
print(facts_2)
print(facts_3)

