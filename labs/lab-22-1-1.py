# Lab 22.1 Task 1
# Task 1 - Interact with eAPI from Python

import requests
from requests.auth import HTTPBasicAuth
import json

auth = HTTPBasicAuth('ntc', 'ntc123')
headers = {
    'Content-Type': 'application/json'
}

payload = {
    "jsonrpc": "2.0",
    "method": "runCmds",
    "params": {
        "format": "json",
        "timestamps": False,
        "cmds": [
            "show version"
        ],
        "version": 1
    },
    "id": "EapiExplorer-1"
}

url = 'http://eos-spine1/command-api'

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)

rsp = response.text

print('\nResponse', '-' * 20)
print(rsp)

print('\nPretty Print Response', '-' * 20)
data = json.loads(response.text)
print(json.dumps(data, indent=4))

print('\nMAC Address', '-' * 20)
print(data['result'][0]['systemMacAddress'])

print('\nMAC Address 2', '-' * 20)
result = data['result'][0]
print(result.get('systemMacAddress'))

payload = {
    "jsonrpc": "2.0",
    "method": "runCmds",
    "params": {
        "format": "json",
        "timestamps": False,
        "cmds": [
            "show vlan brief"
        ],
        "version": 1
    },
    "id": "EapiExplorer-1"
}

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)

data = json.loads(response.text)

print('\nPretty Print Response VLAN', '-' * 20)
print(json.dumps(data, indent=4))

print('\nPrint Response VLAN Name', '-' * 20)
vlans = data['result'][0]
print(vlans['vlans']['1']['name'])