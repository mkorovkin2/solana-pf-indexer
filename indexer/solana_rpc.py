import requests
from config import RPC_URL

def get_block(slot):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBlock",
        "params": [slot, {"transactionDetails": "full", "rewards": False}]
    }
    response = requests.post(RPC_URL, json=payload)
    response.raise_for_status()
    return response.json().get("result")


def get_latest_slot():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSlot"
    }
    response = requests.post(RPC_URL, json=payload)
    response.raise_for_status()
    return response.json().get("result")
