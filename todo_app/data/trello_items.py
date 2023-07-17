import requests
import json
import os

headers = {"Accept": "application/json"}
api_key = os.getenv('TRELLO_KEY')
api_token = os.getenv('TRELLO_TOKEN')

def get_lists():
    url = f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/lists"

    query = {
        'key': api_key,
        'token': api_token,
        'fields': 'name',
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
    return response_json

def get_trello_items():
    response_json = get_lists()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            cards.append(card)
    return cards

def get_to_do_list():
    response_json = get_lists()
    print(response_json)
    
def add_trello_item(name):
    url = "https://api.trello.com/1/cards"

    query = {
        'idList': '5abbe4b7ddc1b351ef961414',
        'key': api_key,
        'token': api_token
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