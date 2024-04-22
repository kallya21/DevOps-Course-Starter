import pytest
import mongomock
from dotenv import load_dotenv, find_dotenv
from todo_app import app
from todo_app.data.db_items import add_todo_item

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
    add_todo_item("Test item")

    response = client.get('/')

    assert response.status_code == 200
    assert b'Test item' in response.data