import subprocess
import os

def title(title):
    return print('\n', title, '-' * 20)

# ==========================================
# Task 1 - Read Network Configuration Files
# ==========================================

# Step 1-1
# From the home directory, navigate to the files directory:

title('Step 1-1')

# Command:
# cd /home/ntc/files/

subprocess.Popen('cd /home/ntc/files/', shell=True)

os.chdir('/home/ntc/files/')

# Step 1-2
# Either by using cat on the terminal (in a different terminal session) or your text editor take a look at the vlan_ids.conf file that is located in the files directory. You'll see that the file looks like this

title('Step 1-2')

# Command:
# cat vlan_ids.conf

subprocess.Popen('cat vlan_ids.conf', shell=True)

# Step 1-3
# Enter into the Python shell while you're in the files directory.

title('Step 1-3')

# Command:
# python

# Step 1-4
# Open the vlan_ids.conf file for reading and use the variable name vlan_file as the file object.

title('Step 1-4')

vlan_file = open('vlan_ids.conf', 'r')

# Step 1-5
# View the type of the newly created object.

title('Step 1-5')

print(type(vlan_file))

# Step 1-6
# Just like you've seen with string, lists, dictionaries, and other common data types, you can also view built-in methods for _io.TextIOWrapper objects.

title('Step 1-6')

print(dir(vlan_file))

# Step 1-7
# Since the file is still open, read all data as a list using the built-in method called read. Use the variable name data.

title('Step 1-7')

data = vlan_file.read()

# Step 1-8
# Print the variable called data

title('Step 1-8')

print(data)

# Step 1-9
# Close the file properly using the close method.

title('Step 1-9')

vlan_file.close()

# ==========================================
# Task 2 - Write to a Configuration File
# ==========================================

# Step 2-1
# Open a file for writing using the "w" value instead "r" for reading:

title('Step 2-1')

out_file = open('interface.cfg', 'w')

# Step 2-2
# The last task used the read method. This task uses the write method.
# Take note that you need to explicitly tell Python to go to the next line using \n after each command (or line) added.
# Add 3 interface commands and write them to the file

title('Step 2-2')

out_file.write("interface Eth1\n")
out_file.write(" speed 100\n")
out_file.write(" duplex full\n")

# Step 2-3
# Close the file for writing

title('Step 2-3')

out_file.close()

# Step 2-4
# In another terminal window, use cat to view the file just created

title('Step 2-4')

# Command:
# cd files/
# cat interface.cfg

subprocess.Popen('cat interface.cfg', shell=True)

# ==========================================
# Task 3 - Use a Context Manager
# ==========================================

# Step 3-1
# The following is the same example as above showing it using the with statement:

title('Step 3-1')

with open("interfaces_2.cfg", "w") as out_file:
    out_file.write("interface Eth2\n")
    out_file.write(" speed 10\n")
    out_file.write(" duplex half\n")

# Step 3-2
# Here is also another example to try for reading the file using the context manager

title('Step 3-2')

with open("interfaces_2.cfg", "r") as vlan_file:
    data = vlan_file.read()

print(data)