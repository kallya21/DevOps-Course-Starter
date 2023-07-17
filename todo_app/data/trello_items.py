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
    list_id = []
    for trello_list in response_json:
        list_id.append(trello_list['id'])
    to_do_list_id = list_id[0]
    return to_do_list_id
    
def add_trello_item(name):
    to_do_list_id = get_to_do_list()
    url = "https://api.trello.com/1/cards"

    query = {
        'idList': to_do_list_id,
        'key': api_key,
        'token': api_token,
        'name': name
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    response_json = response.json()
    print(response_json)

def update_item_status():
    pass