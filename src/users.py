class User:
    def __init__(self, name: str):
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0
        self.next = None

    def borrows_from(self, user: str, amount: float):
        """ the first case takes care of when "x" is borrowing from "y" but
        "y" is owing "x", so it just decreases the amount
        "y" is owing "x" and only puts the remaining amount on "x.owed_by". """

        if user in self.owed_by.keys():
            self.owed_by[user] -= amount
            if self.owed_by[user] <= 0:
                if user not in self.owes.keys():
                    self.owes[user] = 0
                self.owes[user] += abs(
                    self.owed_by[user])
                self.owed_by.pop(user)
                if self.owes[user] == 0:
                    self.owes.pop(user)
        elif user in self.owes.keys():
            self.owes[user] += amount
        else:
            self.owes[user] = amount
        self.adjust_balance()
        return self

    def lends_to(self, user: str, amount: float):
        """ the first case takes care of when "x" owes "y" but
        "y" already owes "x", so it just decreases the amount
        "y" owes to "x" and only puts the remaining amount on "x.owes"."""

        if user in self.owes.keys():
            self.owes[user] -= amount
            if self.owes[user] <= 0:
                if user not in self.owed_by.keys():
                    self.owed_by[user] = 0
                self.owed_by[user] += abs(
                    self.owes[user])
                self.owes.pop(user)
                if self.owed_by[user] == 0:
                    self.owed_by.pop(user)
        elif user in self.owed_by.keys():
            self.owed_by[user] += amount
        else:
            self.owed_by[user] = amount
        self.adjust_balance()
        return self

    def adjust_balance(self):
        tot = 0
        for name in self.owes.keys():
            tot += self.owes[name]
        for name in self.owed_by.keys():
            tot -= self.owed_by[name]
        self.balance = tot
        return tot


class Users:
    """ User list to handle the task."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_user(self, name: str):
        if self.is_unique(name) is False:
            raise Exception(f"{name} already present in the list.")
        if self.head is None:
            self.head = User(name)
            temp_user = self.head
        elif self.tail is None:
            self.tail = User(name)
            self.head.next = self.tail
            temp_user = self.tail
        else:
            self.tail.next = User(name)
            self.tail = self.tail.next
            temp_user = self.tail
        return temp_user

    def is_unique(self, name: str):
        for user in self.navigate_list():
            if user.name == name:
                return False
        return True

    def add_iou(self, lender_name: str, borrower_name: str, amount: float):
        """ Handles the operation of adding the "iou" entirely. """

        lender = self.search_name(lender_name)
        borrower = self.search_name(borrower_name)

        if lender is None:
            raise Exception(f"{lender_name} not found. Add it first!")
        elif borrower is None:
            raise Exception(f"{borrower_name} not found. Add it first!")

        lender.lends_to(borrower_name, amount)
        borrower.borrows_from(lender_name, amount)

        return [lender, borrower]

    def delete_user(self, name: str):
        """ If head is the user to be deleted, deletes it.
        Else it checks user.next recursively till when it's found."""

        if self.head.name == name:
            self.head = self.head.next
        else:
            for user in self.navigate_list():
                if user.next:
                    if user.next.name == name:
                        user.next = user.next.next
        return self.search_name(name)

    def print_list(self):
        print(self.gib_list())
        return self.gib_list()

    def search_name(self, name: str):
        for node in self.navigate_list():
            if node.name == name:
                return node
        return None

    def navigate_list(self):
        nav = self.head
        while nav is not None:
            yield nav
            nav = nav.next

    def gib_list(self, name: str = None):
        """ Returns the users in a list-of-dict format
        or dict format if name != None. """

        if self.head is None:
            raise Exception("User list is empty.")

        if name is None:
            obj_list = []
            for item in self.navigate_list():
                obj_list.append({
                    "name": item.name,
                    "owes": item.owes,
                    "owed_by": item.owed_by,
                    "balance": item.balance
                })
            return obj_list
        else:
            item = self.search_name(name)
            if item is None:
                return None
            return {
                "name": item.name,
                "owes": item.owes,
                "owed_by": item.owed_by,
                "balance": item.balance
            }
