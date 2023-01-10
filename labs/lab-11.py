import subprocess
import os

def title(title):
    return print('\n', title, '-' * 20)

# ==========================================
# Task 1 - Hello Network Automation
# ==========================================

# Step 1-1
# Within your home directory, create a new directory called labs and within it, a sub-directory called python

title('Step 1-1')

subprocess.Popen('mkdir -p /home/ntc/labs/python', shell=True)

# Step 1-2
# Navigate to the python directory.

title('Step 1-2')

subprocess.Popen('cd /home/ntc/labs/python', shell=True)

os.chdir('/home/ntc/labs/python')

# Step 1-3
# Create a new file called networkauto.py

title('Step 1-3')

subprocess.Popen('touch networkauto.py', shell=True)

# Step 1-4
# Open the file in the text editor of your choice.

title('Step 1-4')

# Step 1-5
# Create a Hello World script that just prints Hello Network Automation! - add the following code to the networkauto.py file:

title('Step 1-5')

with open("networkauto.py", "w") as script:
    script.write("print('Hello Network Automation!')\n")

# Step 1-6
# Save the file and execute it from the command line:

title('Step 1-6')   

subprocess.Popen('python networkauto.py', shell=True)

# ==========================================
# Task 2 - Print Data from a Script
# ==========================================

# Step 2-1
# Create a new file called print_facts.py in the /home/ntc/labs/python directory.

title('Step 2-1')

subprocess.Popen('touch print_facts.py', shell=True)

# Step 2-2
# Take the code below and paste it in print_facts.py. Don't forget to save the file!

title('Step 2-2')

string = "import json\nfacts1 = {'vendor': 'cisco', 'os': 'nxos', 'ipaddr': '10.1.1.1'}\nfacts2 = {'vendor': 'cisco', 'os': 'ios', 'ipaddr': '10.2.1.1'}\nfacts3 = {'vendor': 'arista', 'os': 'eos', 'ipaddr': '10.1.1.2'}\ndevices = [facts1, facts2, facts3]\nprint(json.dumps(devices, indent=4))"

with open("print_facts.py", "w") as script:
    script.write(string)

# Step 2-3
# Execute the script.

title('Step 2-3')

subprocess.Popen('python print_facts.py', shell=True)