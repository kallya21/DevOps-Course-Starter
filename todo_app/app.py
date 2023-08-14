from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_trello_items, add_trello_item, update_item_status
from todo_app.data.view_model import ViewModel

app = Flask(__name__)
app.config.from_object(Config())
load_dotenv()

@app.route('/')
def index():
    items = get_trello_items()
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model)

@app.route('/', methods=['POST'])
def new_item():
    item = request.form.get('new_item')
    add_trello_item(item)
    return redirect('/')

@app.route('/complete_item/<card_id>', methods=['POST'])
def complete_item(card_id):
    update_item_status(card_id)
    return redirect('/')