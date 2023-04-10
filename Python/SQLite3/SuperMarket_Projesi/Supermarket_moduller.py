import sqlite3
import time

class item():
    def __init__(self, name, price, counts):
        self.name = name
        self.price = price
        self.counts = counts

    def __str__(self):
        return f"Item Name: {self.name} / Price: {self.price} / Count(s): {self.counts}"

class reyons():
    def __init__(self):
        self.sq_connection()
    def sq_connection(self):
        self.connection = sqlite3.connect("items.db")
        self.cursor = self.connection.cursor()

        create_table = "CREATE TABLE IF NOT EXISTS items (name TEXT, price FLOAT, counts INT)"

        self.cursor.execute(create_table)

        self.connection.commit()
    def sq_disconnection(self):
        self.connection.close()

    def search_item(self, name):
        checkitem = self.cursor.execute("SELECT * FROM items WHERE name = ?", (name,)).fetchall()

        if len(checkitem) != 0:
            searched_item = item(checkitem[0][0], checkitem[0][1], checkitem[0][2])
            print(searched_item)
        else:
            print("Item Doesn't Exısts")
            return False

    def new_item(self, product):
        check_item = self.cursor.execute("SELECT * FROM items where name = ?", (product.name,)).fetchall()

        if len(check_item) == 0:
            add_item = "INSERT INTO items VALUES(?, ?, ?)"
            list1 = product.name, product.price, product.counts
            self.cursor.execute(add_item, list1)
            self.connection.commit()
            print("The item has been added => ", list1)
        else:
            print("The item already exists.. Cannot be added again ! ")

    def increase_count(self, name, counts):
        self.cursor.execute("UPDATE items SET counts = ? WHERE = ?", (counts,name))
        self.connection.commit()
        print("Counts Updated")

    def delete_item(self, name):
        self.cursor.execute("DELETE FROM items WHERE name = ?", (name,))
        print("The item has been deleted..")

    def all_items(self):
        items = self.cursor.execute("SELECT * FROM items").fetchall()
        for i in items:
            print(i)





