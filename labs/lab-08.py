def title(title):
    return print('\n', title, '-' * 20)

# ==========================================
# Task 1 - Use the json module
# ==========================================

# Step 1-1
# Create a dictionary called facts

title('Step 1-1')
print('Create a dictionary called facts\n')
print(">>> facts = {'platform': 'nexus', 'version': '7.3', 'vendor': 'cisco', 'device_type': 'switch', 'os': 'nxos'}")

facts = {'platform': 'nexus', 'version': '7.3', 'vendor': 'cisco', 'device_type': 'switch', 'os': 'nxos'}

# Step 1-2
# Print the dictionary

title('Step 1-2')
print('Print the dictionary\n')
print(">>> print(facts)")

print(facts)

# Step 1-3
# First, import the json module using the import keyword

title('Step 1-3')
print('First, import the json module using the import keyword\n')
print(">>> import json")

import json

# Step 1-4
# Using the dumps function in the json module to pretty print the dictionary. We'll use an indent of 4

title('Step 1-4')
print("Using the dumps function in the json module to pretty print the dictionary. We'll use an indent of 4\n")
print(">>> json.dumps(facts, indent=4)")

print(json.dumps(facts, indent=4))

# Step 1-5
# We'll use 4 spaces as a sane default for every example in the course, but feel free to try 10 and 20 and see what happens:

title('Step 1-5')
print("We'll use 4 spaces as a sane default for every example in the course, but feel free to try 10 and 20 and see what happens\n")
print(">>> json.dumps(facts, indent=10)")

print(json.dumps(facts, indent=10))

print(">>> json.dumps(facts, indent=20)")

print(json.dumps(facts, indent=20))

# ==========================================
# Task 2 - Use the time module
# ==========================================

# Step 2-1
# Import the time module

title('Step 2-1')
print('Import the time module\n')
print(">>> import time")

import time

# Step 2-2
# Insert a pause for 5 seconds using the sleep function

title('Step 2-2')
print('Insert a pause for 5 seconds using the sleep function\n')
print(">>> time.sleep(5)")

time.sleep(5)

# Step 2-3
# Explore printing the date and time with the time module.
# First, do a dir(time). You'll see there are many objects within the time module

title('Step 2-3')
print('Explore printing the date and time with the time module.')
print("First, do a dir(time). You'll see there are many objects within the time module\n")
print(">>> local_time = time.asctime()")

local_time = time.asctime()

print(">>> print(local_time)")

print(local_time)

# ==========================================
# Task 3 - Use the os module
# ==========================================

# Step 3-1
# Import the os module

title('Step 3-1')
print('Import the os module\n')
print(">>> import os")

import os

# Step 3-2
# You can check to see your current working directory with the getcwd() function

title('Step 3-2')
print('You can check to see your current working directory with the getcwd() function\n')
print(">>> os.getcwd()")

print(os.getcwd())

# Step 3-3
# You can also change your working directory with chdir()

title('Step 3-3')
print('You can also change your working directory with chdir()\n')
print(">>> os.chdir('/home/ntc/files')")

os.chdir('/home/ntc/files')

print(">>> os.getcwd()")

print(os.getcwd())

# Step 3-4
# You can also access your OS ENVIRONMENT variables. Here we're accessing an environment variable called HOME

title('Step 3-4')
print("You can also access your OS ENVIRONMENT variables. Here we're accessing an environment variable called HOME\n")
print(">>> os.getenv('HOME')")

print(os.getenv('HOME'))

# Step 3-5
# You can also list the contents of a given directory from Python

title('Step 3-5')
print("You can also list the contents of a given directory from Python\n")
print(">>> os.listdir('/home/ntc')")

print(os.listdir('/home/ntc'))

# Step 3-6
# You can even issue arbitrary Linux commands from Python

title('Step 3-6')
print("You can even issue arbitrary Linux commands from Python\n")
print(">>> os.system('date')")

print(os.system('date'))

print(">>> os.system('ifconfig')")

print(os.system('ifconfig'))
