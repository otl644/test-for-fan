from typing import Dict
from fastapi import FastAPI
from src.data_handler import get_data, write_data_out

users_list = get_data()  # initializing list from db
app = FastAPI()


@app.get("/users")
def get_users(usr_list: Dict, db=users_list):
    usrs = usr_list["users"]
    if len(usrs) == 1:
        return db.gib_list(usrs[0])
    found = []
    for i in range(len(usrs)):
        found.append(db.gib_list(usrs[i]))
    return found


@app.post("/user")
def post_user(user: Dict, db=users_list):
    added_user = db.add_user(user["user"])
    write_data_out(db)
    return db.gib_list(added_user.name)


@app.post("/iou")
def post_iou(info: Dict, db=users_list):
    lender = info["lender"]
    borrower = info["borrower"]
    amount = info["amount"]
    [new_lender, new_borrower] = db.add_iou(lender, borrower, amount)
    write_data_out(db)
    list_to_return = [db.gib_list(new_lender.name),
                      db.gib_list(new_borrower.name)]
    return list_to_return


@app.delete("/user")
def delete_user(user: Dict, db=users_list):
    to_del_user = user["user"]
    db.delete_user(to_del_user)
    write_data_out(db)
    return {"success": True, "msg": "User delete succesfully."}
