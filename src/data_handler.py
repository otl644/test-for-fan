import json
import os
from src.users import Users
from typing import Dict

URL_to_real_db = "storage/db.json"


def write_data_out(user_list, URL=URL_to_real_db):
    with open(URL, "w") as f:
        f.write(json.dumps(user_list.gib_list()))
    return user_list


def check_db_existance(func, URL=URL_to_real_db):
    if os.stat(URL).st_size == 0:
        raise Exception("Couldn't find any db.")
    return func


@check_db_existance
def get_data(URL=URL_to_real_db):
    with open(URL) as f:
        data = json.loads(f.read())
        return structure_in_data(data)


def structure_in_data(data: Dict):
    temp = Users()
    for item in data:
        user = temp.add_user(item["name"])
        if len(item["owes"]) > 0:
            user.owes = item["owes"]
        if len(item["owed_by"]) > 0:
            user.owed_by = item["owed_by"]
        user.adjust_balance()
    return temp
