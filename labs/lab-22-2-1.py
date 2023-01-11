import requests
from requests.auth import HTTPBasicAuth
import json

def hit_api(payload):

    auth = HTTPBasicAuth('ntc', 'ntc123')

    headers = {
        'Content-Type': 'application/json'
    }

    url = 'https://nxos-spine1/ins'

    requests.packages.urllib3.disable_warnings()

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth, verify=False)

    return response.text

payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show version",
        "output_format": "json"
    }
}

response = hit_api(payload)

print('\nResponse', '-' * 20)
print(response)

print('\nPretty Print Response', '-' * 20)
data = json.loads(response)
print(json.dumps(data, indent=4))

print('\nPrint Kickstart Ver Str', '-' * 20)
print(data['ins_api']['outputs']['output']['body']['kickstart_ver_str'])

body = data['ins_api']['outputs']['output']['body']

print('\nPrint Kickstart Ver Str 2', '-' * 20)
print(body.get('kickstart_ver_str'))

payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show vlan brief",
        "output_format": "json"
    }
}

response = hit_api(payload)

data = json.loads(response)

print('\nPrint Show Vlan', '-' * 20)
print(json.dumps(data, indent=4))

vlans = data['ins_api']['outputs']['output']['body']

print('\nPrint Show Vlan 2', '-' * 20)
print(json.dumps(vlans, indent=4))

print('\nPrint Show Vlan Name 0', '-' * 20)
print(vlans['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief'][0]['vlanshowbr-vlanname'])

print('\nPrint Show Vlan Name 1', '-' * 20)
print(vlans['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief'][1]['vlanshowbr-vlanname'])