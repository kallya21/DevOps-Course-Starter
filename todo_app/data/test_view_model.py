import pytest
from todo_app.data.view_model import ViewModel
from todo_app.data.trello_items import Item

@pytest.fixture
def sample_items():
    return [
        Item(1, "NAME1", "To Do"),
        Item(2, "NAME2", "To Do"),
        Item(3, "NAME3", "To Do"),
        Item(4, "NAME4", "Doing"),
        Item(5, "NAME5", "Done"),
        Item(6, "NAME6", "Done"),
        Item(7, "NAME7", "Done"),
    ]

def test_view_model_done_property(sample_items):
    view_model = ViewModel(sample_items)
    done_list = view_model.done_items

    assert len(done_list) == 3

    for item in done_list:
        assert item.status == "Done"

def test_view_model_doing_property(sample_items):
    view_model = ViewModel(sample_items)
    doing_list = view_model.doing_items

    assert len(doing_list) == 1

    for item in doing_list:
        assert item.status == "Doing"

def test_view_model_to_do_property(sample_items):
    view_model = ViewModel(sample_items)
    to_do_list = view_model.to_do_items

    assert len(to_do_list) == 3

    for item in to_do_list:
        assert item.status == "To Do"
