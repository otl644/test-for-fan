from src.data_handler import write_data_out, get_data
from src.users import Users
import pytest


URL = "storage/test_db.json"


@pytest.fixture()
def init():
    temp = Users()
    temp.add_user("Adam")
    temp.add_user("Bob")
    temp.add_user("Carl")
    temp.add_iou("Adam", "Bob", 4)
    temp.add_iou("Carl", "Bob", 4)
    temp.add_iou("Adam", "Bob", 4)
    temp.add_iou("Bob", "Carl", 3.4)
    temp.add_iou("Bob", "Adam", 3)
    return write_data_out(temp, URL)


def test_get_data(init):
    assert init.gib_list() == get_data(URL).gib_list()


def test_get_data_fail(init):
    with pytest.raises(Exception):
        get_data("emptydb.json")


@pytest.mark.parametrize("test_input", [
    ("Giuseppe")
])
def test_write_data(init, test_input):
    init.add_user(test_input)
    wrote_list = write_data_out(init, URL)

    assert wrote_list.gib_list() == get_data(URL).gib_list()
