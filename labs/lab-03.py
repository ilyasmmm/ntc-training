def title(title):
    return print('\n', '-' * 5, title, '-' * 5)

# ==========
# Task 1 - Explore Basic String Operations
# ==========

# ---
# STEP 1-1
title("STEP 1-1")

print(">>> ")
print(">>> hostname = 'CORESWITCH-A'")
print(">>> ")

hostname = 'CORESWITCH-A'

# ---
# STEP 1-2
title("STEP 1-2")

print(">>> type(hostname)")
print(type(hostname))
print(">>> ")

# ---
# STEP 1-3
title("STEP 1-3")

print(">>> hostname.lower()")
print(hostname.lower())
print(">>> ")

# ---
# STEP 1-4
title("STEP 1-4")

print(">>> lower_hostname = hostname.lower()")
lower_hostname = hostname.lower()
print(">>> ")
print(">>> print(lower_hostname)")
print(lower_hostname)
print(">>> ")

# ---
# STEP 1-5
title("STEP 1-5")

print('>>> interface_config = "interface Eth1\n duplex full\n speed 100"'.encode())
interface_config = "interface Eth1\n duplex full\n speed 100"
print(">>> ")

# ---
# STEP 1-6
title("STEP 1-6")

print('>>> interface_config')
print(interface_config.encode())
print(">>> ")
print(">>> print(interface_config)")
print(interface_config)
print(">>> ")

# ---
# STEP 1-7
title("STEP 1-7")

print(">>> ")
print(">>> ip_addr = '10.20.5.5'")
ip_addr = '10.20.5.5'
print(">>> ")

# ---
# STEP 1-8
title("STEP 1-8")

print(">>> ")
print(">>> ip_addr.replace('5', '100')")
print(ip_addr.replace('5', '100'))
print(">>> ")

# ---
# STEP 1-9
title("STEP 1-9")

print(">>> ")
print(">>> ip_addr.replace('5', '100', 1)")
print(ip_addr.replace('5', '100', 1))
print(">>> ")

# ---
# STEP 1-10
title("STEP 1-10")

print(">>> ip_addr2 = ip_addr.replace('5', '100')")
ip_addr2 = ip_addr.replace('5', '100')
print(">>> ")
print(">>> print(ip_addr2)")
print(ip_addr2)
print(">>> ")

# ---
# STEP 1-11
title("STEP 1-11")

print(">>> dir(ip_addr2)")
print(dir(ip_addr2))
print(">>> ")
print(">>> dir(str)")
print(dir(str))
print(">>> ")

# ---
# STEP 1-12
title("STEP 1-12")

print(">>> help(str.upper)")
print(help(str.upper))
print(">>> ")
print(">>> help(str.replace)")
print(help(str.replace))
print(">>> ")
print(">>> help(str.split)")
print(help(str.split))
print(">>> ")

# ---
# STEP 1-13
title("STEP 1-13")

print(">>> octets = ip_addr2.split('.')")
octets = ip_addr2.split('.')

print(">>> ")
print(">>> print(octets)")
print(octets)
print(">>> ")
print(">>> print(octets[0])")
print(octets[0])
print(">>> ")
print(">>> print(octets[1])")
print(octets[1])
print(">>> ")
print(">>> print(octets[2])")
print(octets[2])
print(">>> ")
print(">>> print(octets[3])")
print(octets[3])
print(">>> ")
    
# ---
# STEP 1-14
title("STEP 1-14")

print(">>> print(type(octets))")
print(type(octets))
print(">>> ")

# ==========
# Task 2 - Extract String Contents
# ==========

# ---
# STEP 2-1
title("STEP 2-1")

print(">>> interface = 'Ethernet1/10'")
interface = 'Ethernet1/10'
print(">>> ")

# ---
# STEP 2-2
title("STEP 2-2")

print(">>> interface.lstrip('Ethernet')")
print(interface.lstrip('Ethernet'))
print(">>> ")

# ---
# STEP 2-3
title("STEP 2-3")

print(">>> int_id = interface.lstrip('Ethernet')")
int_id = interface.lstrip('Ethernet')
print(">>> ")
print(">>> int_id")
print(int_id)
print(">>> ")

# ---
# STEP 2-4
title("STEP 2-4")

print(">>> slot = int_id.split('/')[0]")
slot = int_id.split('/')[0]
print(">>> ")
print(">>> intf = int_id.split('/')[1]")
intf = int_id.split('/')[1]
print(">>> ")

# ---
# STEP 2-5
title("STEP 2-5")

print(">>> parsed_interface = int_id.split('/')")
parsed_interface = int_id.split('/')
print(">>> ")
print(">>> parsed_interface")
print(parsed_interface)
print(">>> ")
print(">>> slot = parsed_interface[0]")
slot = parsed_interface[0]
print(">>> ")
print(">>> intf = parsed_interface[1]")
intf = parsed_interface[1]
print(">>> ")

# ---
# STEP 2-6
title("STEP 2-6")

print(">>> slot.isdigit()")
print(slot.isdigit())
print(">>> ")
print(">>> intf.isdigit()")
print(intf.isdigit())
print(">>> ")
    
# ==========
# Task 3 - Format String Output
# ==========

# ---
# STEP 3-1
title("STEP 3-1")

print(">>> speed = '1000'")
speed = '1000'
print(">>> ")
print(">>> duplex = 'full'")
duplex = 'full'
print(">>> ")
print(">>> description = 'Uplink Interface Configured by Python'")
description = 'Uplink Interface Configured by Python'
print(">>> ")

# ---
# STEP 3-2
title("STEP 3-2")

print(">>> speed_cmd = 'speed {}'.format(speed)")
speed_cmd = 'speed {}'.format(speed)
print(">>> ")
print(">>> duplex_cmd = 'duplex {}'.format(duplex)")
duplex_cmd = 'duplex {}'.format(duplex)
print(">>> ")
print(">>> descr_cmd = 'description {}'.format(description)")
descr_cmd = 'description {}'.format(description)
print(">>> ")

# ---
# STEP 3-3
title("STEP 3-3")

print(">>> print(speed_cmd)")
print(speed_cmd)
print(">>> ")
print(">>> print(duplex_cmd)")
print(duplex_cmd)
print(">>> ")
print(">>> print(descr_cmd)")
print(descr_cmd)
print(">>> ")

# ---
# STEP 3-4
title("STEP 3-4")

print('>>> default_gw = "10.{}.10.1"')
default_gw = "10.{}.10.1"
print(">>> ")

# ---
# STEP 3-5
title("STEP 3-5")

print('>>> site_id = "20"')
site_id = "20"
print(">>> ")

# ---
# STEP 3-6
title("STEP 3-6")

print(">>> default_gw.format(site_id)")
print(default_gw.format(site_id))
print(">>> ")

# ---
# STEP 3-7
title("STEP 3-7")

print('>>> site_id = "30"')
site_id = "30"
print(">>> ")
print(">>> default_gw.format(site_id)")
print(default_gw.format(site_id))
print(">>> ")

# ---
# STEP 3-8
title("STEP 3-8")

print('>>> service_id = "100"')
service_id = "100"
print(">>> ")
print('>>> node_id = "1"')
node_id = "1"
print(">>> ")
print('>>> mask = "24"')
mask = "24"
print(">>> ")

# ---
# STEP 3-9
title("STEP 3-9")

print('>>> default_gw = f"10.{site_id}.{service_id}.{node_id}/{mask}"')
print(">>> ")
print(">>> default_gw")
print(default_gw)
print(">>> ")

# ---
# STEP 3-10
title("STEP 3-10")

print('>>> "{} {} {}".format("Hostname", "Location", "Vendor")')
print("{} {} {}".format("Hostname", "Location", "Vendor"))
print(">>> ")
print('>>> "{:12} {:12} {:12}".format("Hostname", "Location", "Vendor")')
print("{:12} {:12} {:12}".format("Hostname", "Location", "Vendor"))
print(">>> ")
print('>>> "{:12} {:12} {:12}".format("nyc-rt01", "New York", "Cisco")')
print("{:12} {:12} {:12}".format("nyc-rt01", "New York", "Cisco"))
print(">>> ")
print('>>> f"{\'nyc-rt02\':12} {\'New York\':12} {\'Juniper\':12}"')
print(f"{'nyc-rt02':12} {'New York':12} {'Juniper':12}")
print(">>> ")