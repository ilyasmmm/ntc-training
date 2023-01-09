def title(title):
    return print('\n', '-' * 5, title, '-' * 5)

# ==========
# Task 1 - Explore Basic Integer Operations
# ==========

# ---
# STEP 1-1
title("STEP 1-1")

print('>>> ')
print('>>> vlan_id = 10')
vlan_id = 10
print('>>> ')

# ---
# STEP 1-2
title("STEP 1-2")

print('>>> type(vlan_id)')
print(type(vlan_id))
print('>>> ')

# ---
# STEP 1-3
title("STEP 1-3")

print('>>> dir(vlan_id)')
print(dir(vlan_id))
print('>>> ')

# ---
# STEP 1-4
title("STEP 1-4")

print('>>> vid = "100"')
vid = "100" 
print('>>> ')

# ---
# STEP 1-5
title("STEP 1-5")

print('>>> print(vlan_id)')
print(vlan_id)
print('>>> ')
print('>>> print(vid)')
print(vid)
print('>>> ')

# ---
# STEP 1-6
title("STEP 1-6")

print('>>> vlan_id')
print(vlan_id)
print('>>> ')
print('>>> vid')
print(vid.encode())
print('>>> ')

# ---
# STEP 1-7
title("STEP 1-7")

print('>>> ipaddr = "10.2.9.1"')
ipaddr = "10.2.9.1"
print('>>> ')
print('>>> mask = 24')
mask = 24
print('>>> ')

# ---
# STEP 1-8
title("STEP 1-8")

try:
    print('>>> ipaddr = ipaddr + "/" + mask')
    ipaddr = ipaddr + "/" + mask
except Exception as e:
    print(e)
    print('>>> ')

# ---
# STEP 1-9
title("STEP 1-9")

print('>>> ipaddr + "/" + str(mask)')
print(ipaddr + "/" + str(mask))
print('>>> ')

# ---
# STEP 1-10
title("STEP 1-6")

print('>>> type(vlan_id)')
print(type(vlan_id))
print('>>> ')
print('>>> vlan_id_string = str(vlan_id)')
vlan_id_string = str(vlan_id)
print('>>> ')
print('>>> type(vlan_id_string)')
print(type(vlan_id_string))
print('>>> ')