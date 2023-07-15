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
        'token': os.getenv('TRELLO_TOKEN'),
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

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            cards.append(card)

        print(cards)