import requests
import json
import os

def get_trello_items():
    url = f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/lists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': os.getenv('TRELLO_KEY'),
        'token': os.getenv('TRELLO_TOKEN')
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))