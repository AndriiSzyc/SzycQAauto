import pytest



@pytest.mark.database
def test_database_connection(db):
    """test to check database connection"""
    answer = db.test_connection()
    print(f"Connected successfully. SQLite Database Versio is: {answer}")

    assert isinstance(answer, list)


"""Tests to test the Customers table"""


@pytest.mark.database
def test_check_all_users(db):
    users = db.get_all_users()

    assert users[0][1] == "Maydan Nezalezhnosti 1"
    assert users[1][0] == "Stepan"
    assert users[1][2] == "Kyiv"
    assert users[0][2] == "Kyiv"


@pytest.mark.database
def test_check_user_by_name(db):
    user = db.get_user_by_name("Sergii")

    assert user[0][0] == "Sergii"
    assert user[0][1] == "Maydan Nezalezhnosti 1"
    assert user[0][2] == "Kyiv"
    assert len(user) == 1


@pytest.mark.database
def test_check_address_user_sergii(db):
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"
    assert len(user) == 1


"""Tests to test the Products table"""


@pytest.mark.database
def test_get_all_products(db):
    products = db.get_all_products()

    assert products[0][0] == 1
    assert products[0][2] == "з цукром"
    assert products[1][1] == "солодка вода"
    assert products[1][2] == "з цукрозамінником"
    assert products[2][0] == 3
    assert products[2][1] == "молоко"


@pytest.mark.database
def test_quantity_by_name_and_description_product(db):
    products = db.get_quantity_by_name_and_description_prodact(
        "солодка вода", "з цукром"
    )

    assert products[0][0] == 1
    assert products[0][2] == "з цукром"
    assert len(products) == 1


@pytest.mark.database
def test_product_qnt_update(db):
    db.update_product_qnt_by_ID(1, 25)
    water_qnt = db.select_product_qnt_by_ID(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(db):
    db.insert_product(4, "печево", "солодке", 30)
    water_qnt = db.select_product_qnt_by_ID(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(db):
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_ID(99)
    qnt = db.select_product_qnt_by_ID(99)

    assert len(qnt) == 0


"""Tests to test the Orders table"""


@pytest.mark.database
def test_detailed_orders(db):
    orders = db.get_detailed_orders()
    print("Order", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"
    assert orders[0][4] == "Ukraine"
    assert orders[0][5] == "3127"


@pytest.mark.database
def test_addead_order_to_orders(db):
    db.added_new_order_in_orders(99, "Stepan", "молоко", "12:22:23")
    orders = db.get_detailed_orders()
    print("Order", orders)

    assert orders[1][0] == 99
    assert orders[1][1] == "Stepan"
    assert orders[1][2] == "молоко"
    assert orders[1][3] == "натуральне незбиране"
    assert orders[1][4] == "Ukraine"
    assert orders[1][5] == "2055"


@pytest.mark.database
def test_delete_order_by_ID(db):
    db.added_new_order_in_orders(99, "Stepan", "молоко", "12:22:23")
    db.delet_order_by_ID(99)
    record = db.select_order_by_ID(99)

    assert len(record) == 0



@pytest.mark.database
def test_get_all_date_from_orders(db):
    orders = db.get_all_data_in_orders()
    print(orders)
