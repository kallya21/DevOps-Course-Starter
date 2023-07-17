from flask import Flask, render_template, request, redirect

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items, add_item

from todo_app.data.trello_items import get_trello_items, add_trello_item, get_to_do_list

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    get_to_do_list()
    cards = get_trello_items()
    return render_template('index.html', cards=cards)

@app.route('/', methods=['POST'])
def new_item():
    item = request.form.get('new_item')
    add_trello_item(item)
    return redirect('/')