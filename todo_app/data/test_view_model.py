from todo_app.data.view_model import ViewModel
from todo_app.data.trello_items import Item

def test_view_model_done_property():
    items = [
        Item(1, "NAME1", "To Do"),
        Item(2, "NAME2", "To Do"),
        Item(3, "NAME3", "To Do"),
        Item(4, "NAME4", "To Do"),
        Item(5, "NAME5", "Done"),
        Item(6, "NAME6", "Done"),
        Item(7, "NAME7", "Done"),
    ]
    view_model = ViewModel(items)
    done_list = view_model.done_items
    assert len(done_list) == 3
    for item in done_list:
        assert item.status == "Done"