import pytest
from src.app import get_users, post_iou, post_user, delete_user
from typing import List, Dict


@pytest.mark.parametrize("test_input,output", [
    ({"user": "Adam111"}, "Adam111"),
    ({"user": "Bob111"}, "Bob111"),
    ({"user": "Carlino111"}, "Carlino111"),
    ({"user": "Giuseppino111"}, "Giuseppino111"),
    ({"user": "Giacomo111"}, "Giacomo111")
])
def test_post_users(test_input: Dict, output: str):
    """ Tests if the func returns the wanted output."""
    expected_output = post_user(test_input)["name"]
    assert expected_output == output


@pytest.mark.parametrize("test_input,output", [
    ({"users": ["Adam111", "Bob111"]}, ["Adam111", "Bob111"]),
    ({"users": ["Giuseppino111"]}, "Giuseppino111")
])
def test_get_users(test_input: Dict, output: List):
    """ Initializes the wanted users and then checks
    if they've been retrieved correctly. """

    response = get_users(test_input)

    # there are 2 cases here: one returns a list, one a single dict.
    if type(response) is list:
        out_name_list = []
        for user in response:  # probably can put this inside the []
            out_name_list.append(user["name"])
        assert out_name_list == output
    else:
        assert response["name"] == output


@pytest.mark.parametrize("test_input", [
    {"lender": "Adam111", "borrower": "Bob111", "amount": 5},
    {"lender": "Bob111", "borrower": "Carlino111", "amount": 93.2}
])
def test_post_iou(test_input: Dict):
    """ Compares old balance to new one."""

    old_users = get_users(
        {"users": [test_input["lender"], test_input["borrower"]]})

    users_old_balance = [old_users[0]["balance"], old_users[1]["balance"]]

    new_users = post_iou(test_input)

    users_new_balance = [new_users[0]["balance"], new_users[1]["balance"]]

    assert users_old_balance[0] != users_new_balance[0]
    assert users_old_balance[1] != users_new_balance[1]

    # revert changes
    post_iou({"lender": test_input["borrower"],
              "borrower": test_input["lender"],
              "amount": test_input["amount"]})


@pytest.mark.parametrize("test_input", [
    ({"user": "Adam111"}),
    ({"user": "Bob111"}),
    ({"user": "Carlino111"}),
    ({"user": "Giuseppino111"}),
    ({"user": "Giacomo111"})
])
def test_delete_user(test_input):
    """ Deletes an user and checks if the get fuction still returns it. """
    delete_user(test_input)
    assert get_users({"users": [test_input["user"]]}) is None
