from src.users import Users
import pytest
import math


@pytest.fixture()
def init():
    user_list = Users()
    user_list.add_user("Adam")
    user_list.add_user("Bob")
    user_list.add_user("Carl")
    user_list.add_iou("Adam", "Bob", 5),
    user_list.add_iou("Bob", "Adam", 5),
    user_list.add_iou("Bob", "Adam", 5)
    return user_list


@pytest.mark.parametrize("test_input,output", [
    ('DiffStringType', 'DiffStringType'),
    ("withnb3ers", "withnb3ers"),
    ("with!$%", "with!$%"),
])
def test_add_user(init, test_input, output):
    assert init.add_user(test_input).name == output


@pytest.mark.parametrize("test_input", [
    ("Adam"),
    ("Bob"),
    ("Carl")
])
def test_add_user_fail(init, test_input):
    with pytest.raises(Exception):
        init.add_user(test_input)


@pytest.mark.parametrize("test_input,output", [
    ("Adam", "Adam"),
    ("Bob", "Bob"),
    ("Giuseppina", None)
])
def test_search_name(init, test_input, output):
    if init.search_name(test_input) is not None:
        assert init.search_name(test_input).name == output
    else:
        assert init.search_name(test_input) == output


@pytest.mark.parametrize("test_input", [
    ["Bob", "Adam", 5],
    ["Bob", "Adam", 2.333],
    ["Adam", "Bob", 4/3],
    ["Carl", "Bob", 4/3],
    ["Bob", "Carl", 4/3]
])
def test_iou_op(init, test_input):
    """ I'm testing whether or not the balance changes after adding a "iou",
    which I know isn't the most precise way to assert if the function works
    properly but it's what I chose to go with for productivity's sake. """

    old_lender_balance = init.search_name(test_input[0]).balance
    old_borrower_balance = init.search_name(test_input[1]).balance

    new_lender, new_borrower = init.add_iou(
        test_input[0], test_input[1], test_input[2])

    assert math.isclose(old_lender_balance,
                        new_lender.balance, rel_tol=1e-6) is not True
    assert math.isclose(old_borrower_balance,
                        new_borrower.balance, rel_tol=1e-6) is not True


@pytest.mark.parametrize("test_input", [
    ["fail", "Adam", 4],
    ["Adam", "fail", 4]
])
def test_iou_fails(init, test_input):
    with pytest.raises(Exception):
        if test_input[0] == "fail":
            init.add_iou(test_input)
        elif test_input[1] == "fail":
            init.add_iou(test_input)


def test_navigate(init):
    is_first = True
    found_head = None
    found_tail = None
    for user in init.navigate_list():
        if is_first:
            found_head = user.name
        elif user.next is None:
            found_tail = user.name
        is_first = False
    assert init.head.name == found_head
    assert init.tail.name == found_tail


def test_gib_name(init):
    for user in init.navigate_list():
        assert user.name == init.gib_list(user.name)["name"]


def test_gib_list(init):
    gib_output_len = len(init.gib_list())
    counter = 0
    for item in init.navigate_list():
        counter += 1
    assert gib_output_len == counter


def test_gib_list_fail():
    temp = Users()
    with pytest.raises(Exception):
        temp.gib_list()


def test_gib_list_noname():
    temp = Users()
    with pytest.raises(Exception):
        temp.gib_list("Adam")


def test_print_list(init):
    printed_list = init.print_list()
    for user in printed_list:
        assert user["name"] == init.search_name(user["name"]).name


@pytest.mark.parametrize("test_input", [
    "Adam",
    "Bob",
    "Carl"
])
def test_delete_user(init, test_input):
    init.delete_user(test_input)
    assert init.search_name(test_input) is None
