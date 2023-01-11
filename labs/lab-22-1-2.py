# Lab 22.1
# Task 2 - Gather Neighbors Script

import requests
from requests.auth import HTTPBasicAuth
import json

# Created by Me
def secondary():

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
                "show lldp neighbors"
            ],
            "version": 1
        },
        "id": "EapiExplorer-1"
    }

    spine_list = [ 'eos-spine1', 'eos-spine2' ]

    neighbors_list = {}

    for spine in spine_list:

        url = f'http://{spine}/command-api'

        response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)

        data = json.loads(response.text)

        print(f'\nPretty Print Response | {spine}', '-' * 20)
        print(json.dumps(data, indent=4))

        lldp_neighbors = data['result'][0]['lldpNeighbors']

        neighbors_list[spine] = []

        for neighbor in lldp_neighbors:
            new_neighbor = {
                "neighbor_interface": neighbor["neighborPort"],
                "local_interface": neighbor["port"],
                "neighbor": neighbor["neighborDevice"]
            }
            neighbors_list[spine].append(new_neighbor)

    print('\nPrint Neighbors List', '-' * 20)
    print(json.dumps(neighbors_list, indent=4))

# Challenge Solution
def eapi_request(device, commands):
    auth = HTTPBasicAuth("ntc", "ntc123")
    headers = {"Content-Type": "application/json"}

    url = f"http://{device}/command-api"
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "format": "json",
            "timestamps": False,
            "cmds": commands,
            "version": 1,
        },
        "id": "EapiExplorer-1",
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, auth=auth
    )
    return response


def get_eos_neighbors(response):

    data = json.loads(response.text)

    device_neighbors = data["result"][0]["lldpNeighbors"]

    neighbors_list = []
    for neighbor in device_neighbors:
        new_neighbor = {
            "neighbor_interface": neighbor["neighborPort"],
            "local_interface": neighbor["port"],
            "neighbor": neighbor["neighborDevice"],
        }
        neighbors_list.append(new_neighbor)

    return neighbors_list


def main():

    neighbors = {}

    devices = ["eos-spine1", "eos-spine2"]
    commands = ["show lldp neighbors"]
    for dev in devices:
        response = eapi_request(dev, commands)
        neighbors[dev] = get_eos_neighbors(response)

    print(json.dumps(neighbors, indent=4))


if __name__ == "__main__":
    main()
    secondary()