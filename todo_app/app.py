from flask import Flask, render_template, request, redirect

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/', methods=['POST'])
def new_item():
    item = request.form.get('new_item')
    add_item(item)
    return redirect('/')