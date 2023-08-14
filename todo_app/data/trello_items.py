import requests
import os

class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])

def headers():
    return {"Accept": "application/json"}

def api_key():
    return os.getenv('TRELLO_KEY')

def api_token():
    return os.getenv('TRELLO_TOKEN')

def get_lists():
    url = f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/lists"

    query = {
        'key': api_key(),
        'token': api_token(),
        'fields': 'name',
        'cards': 'open',
        'card_fields': 'id,name'
    }

    response = requests.request(
        "GET",
        url,
        headers=headers(),
        params=query
    )

    response_json = response.json()
    return response_json

def get_trello_items():
    response_json = get_lists()

    items = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            item = Item.from_trello_card(card, trello_list)
            items.append(item)

    return items
    
def add_trello_item(name):
    to_do_list_id = os.getenv('TO_DO_LIST_ID')
    url = "https://api.trello.com/1/cards"

    query = {
        'idList': to_do_list_id,
        'key': api_key(),
        'token': api_token(),
        'name': name
    }

    response = requests.request(
        "POST",
        url,
        headers=headers(),
        params=query
    )

    response_json = response.json()
    return response_json

def update_item_status(card_id):
    done_list_id = os.getenv('DONE_LIST_ID')
    url = f"https://api.trello.com/1/cards/{card_id}"

    query = {
        'key': api_key(),
        'token': api_token(),
        'idList': done_list_id
    }

    response = requests.put(url, params=query)

    response_json = response.json()
    return response_json