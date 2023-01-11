import requests
from requests.auth import HTTPBasicAuth
import json

# ---
# Created by Me

def hit_api(url):

    auth = HTTPBasicAuth('ntc', 'ntc123')

    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show cdp neighbors",
            "output_format": "json"
        }
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth, verify=False)

    return response.text

def secondary():
    spine_list = [ 'nxos-spine1', 'nxos-spine2' ]

    neighbors_list = {}

    for spine in spine_list:

        url = f'https://{spine}/ins'

        response = hit_api(url)

        data = json.loads(response)

        print(f'\nResponse | {spine}', '-' * 20)
        print(json.dumps(data, indent=4))

        cdp_neighbors = data['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']

        if isinstance(cdp_neighbors, dict):
            cdp_neighbors = [cdp_neighbors]

        neighbors_list[spine] = []

        for neighbor in cdp_neighbors:
            new_neighbor = {
                "neighbor_interface": neighbor["port_id"],
                "local_interface": neighbor["intf_id"],
                "neighbor": neighbor["device_id"]
            }
            neighbors_list[spine].append(new_neighbor)

    print('\nNeighbors List', '-' * 20)
    print(json.dumps(neighbors_list, indent=4))

# ---
# Challenge Solution

def nxapi_request(device, command):
    auth = HTTPBasicAuth("ntc", "ntc123")
    headers = {"Content-Type": "application/json"}

    url = f"https://{device}/ins"

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": command,
            "output_format": "json",
        }
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, auth=auth, verify=False
    )
    return response

def get_nxos_neighbors(response):

    data = json.loads(response.text)

    device_neighbors = data["ins_api"]["outputs"]["output"]["body"][
        "TABLE_cdp_neighbor_brief_info"
    ]["ROW_cdp_neighbor_brief_info"]
    if isinstance(device_neighbors, dict):
        device_neighbors = [device_neighbors]

    neighbors_list = []
    for neighbor in device_neighbors:
        neighbor = {
            "neighbor_interface": neighbor["port_id"],
            "local_interface": neighbor["intf_id"],
            "neighbor": neighbor["device_id"],
        }
        neighbors_list.append(neighbor)

    return neighbors_list

def main():

    neighbors = {}

    devices = ["nxos-spine1", "nxos-spine2"]
    command = "show cdp neighbors"
    for dev in devices:
        response = nxapi_request(dev, command)
        neighbors[dev] = get_nxos_neighbors(response)

    print(json.dumps(neighbors, indent=4))

if __name__ == "__main__":

    requests.packages.urllib3.disable_warnings()

    main()
    secondary()