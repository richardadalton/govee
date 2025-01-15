import requests
import json
import os

API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://openapi.api.govee.com"

def get_devices():
    url = BASE_URL + "/router/api/v1/user/devices"
    headers = {
        "Content-Type": "application/json",
        "Govee-API-Key": API_KEY,
    }
    return requests.get(url, headers=headers)


def get_device_state(sku, device):
    url = BASE_URL + "/router/api/v1/device/state"

    headers = {
        "Content-Type": "application/json",
        "Govee-API-Key": API_KEY,
    }

    payload = {
        "requestId": "uuid",
        "payload": {
            "sku": sku,
            "device": device
        }
    }

    return requests.post(url, headers=headers, json=payload)



def parse_response(r):
    return json.loads(r.text)

def main():
    state = parse_response(get_device_state(sku="H5179", device="13:43:3F:9D:09:13:00:EE"))

    print(state)
    for c in state['payload']['capabilities']:
        print(c['instance'], c['state']['value'])


if __name__ == '__main__':
    main()