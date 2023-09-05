import sqlite3


class Database:
    """class for database connection"""

    def __init__(self):
        """create a connection to the database"""
        self.conection = sqlite3.connect(
            "/home/andrii/QAauto/tests_practice/become_qa_auto.db"
        )
        """ order to execute SQL statements and fetch results from SQL queries """
        self.cursor = self.conection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        """ execute query """
        self.cursor.execute(sqlite_select_Query)
        """ fetch the resulting row """
        record = self.cursor.fetchall()
        return record

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers;"
        """ execute query fetch the resulting row """
        record = self.cursor.execute(query).fetchall()
        return record

    def get_user_by_name(self, username):
        query = "SELECT name, address, city FROM customers WHERE name=?"
        record = self.cursor.execute(query, (username,)).fetchall()
        return record

    def get_user_address_by_name(self, username):
        query = "SELECT address, city, postalCode, country FROM customers WHERE name=?"
        record = self.cursor.execute(query, (username,)).fetchall()
        return record

    def get_all_products(self):
        query = "SELECT id, name, description, quantity FROM products;"
        record = self.cursor.execute(query).fetchall()
        return record

    def get_quantity_by_name_and_description_prodact(self, product_name, description):
        query = "SELECT id, name, description, quantity FROM products WHERE name=? AND description=?"
        record = self.cursor.execute(query, (product_name, description)).fetchall()
        return record

    def update_product_qnt_by_ID(self, product_id, qnt):
        query = "UPDATE products SET quantity=? WHERE id=?"
        self.cursor.execute(query, (product_id, qnt))
        self.conection.commit()

    def select_product_qnt_by_ID(self, product_id):
        query = "SELECT quantity FROM products WHERE id=?"
        record = self.cursor.execute(query, (product_id,)).fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = "INSERT OR REPLACE INTO products (id, name, description, quantity)\
             VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (product_id, name, description, qnt))
        self.conection.commit()

    def delete_product_ID(self, product_id):
        query = "DELETE FROM products WHERE id=?"
        self.cursor.execute(query, (product_id,))
        self.conection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, customers.country, customers.postalCode, orders.order_date\
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        record = self.cursor.execute(query).fetchall()
        return record

    def added_new_order_in_orders(self, id, customer_name, product_name, date):
        query = "INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
                VALUES ( ?, (SELECT id FROM customers WHERE name=?), \
                (SELECT id FROM products WHERE name=?), \
                ?)"
        self.cursor.execute(query, (id, customer_name, product_name, date))
        self.conection.commit()

    def delet_order_by_ID(self, order_id):
        query = "DELETE FROM orders WHERE id=?"
        self.cursor.execute(query, (order_id,))
        self.conection.commit()

    def select_order_by_ID(self, product_id):
        query = "SELECT order_date FROM orders WHERE id=?"
        record = self.cursor.execute(query, (product_id,)).fetchall()
        return record

    def get_all_data_in_orders(self):
        query = "SELECT * FROM orders"
        record = self.cursor.execute(query).fetchall()
        return record
