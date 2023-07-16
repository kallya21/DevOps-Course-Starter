import requests
import json
import os

headers = {
    "Accept": "application/json"
}

def get_trello_items():
    url = f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/lists"

    query = {
        'key': os.getenv('TRELLO_KEY'),
        'token': os.getenv('TRELLO_TOKEN'),
        'fields': 'id,name',
        'cards': 'open',
        'card_fields': 'id,name'
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    response_json = response.json()

    print(response_json)

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            cards.append(card)
        print(cards)

def add_trello_item(title):
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': '5abbe4b7ddc1b351ef961414',
        'key': os.getenv('TRELLO_KEY'),
        'token': os.getenv('TRELLO_TOKEN')
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def update_item_status():
    pass