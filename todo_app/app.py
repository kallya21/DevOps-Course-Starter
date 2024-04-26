from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.db_items import get_todo_items, add_todo_item, update_item_status
from todo_app.data.view_model import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = get_todo_items()
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/', methods=['POST'])
    def new_item():
        item = request.form.get('new_item')
        add_todo_item(item)
        return redirect('/')

    @app.route('/complete_item/<item_id>', methods=['POST'])
    def complete_item(item_id):
        update_item_status(item_id)
        return redirect('/')
    
    return app