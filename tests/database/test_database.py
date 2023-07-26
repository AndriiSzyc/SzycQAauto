import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection(sqlite_table_connection):
    sqlite_table_connection.test_connection()


@pytest.mark.database
def test_chek_all_users(sqlite_table_connection):
    users = sqlite_table_connection.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii(sqlite_table_connection):
    user = sqlite_table_connection.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(sqlite_table_connection):
    sqlite_table_connection.update_product_qnt_by_id(1, 25)
    water_qnt = sqlite_table_connection.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(sqlite_table_connection):
    sqlite_table_connection.insert_product(4, "печиво", "солодке", 30)
    water_qnt = sqlite_table_connection.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(sqlite_table_connection):
    sqlite_table_connection.insert_product(99, "tests", "data", 99)
    sqlite_table_connection.delete_product_by_id(99)
    qnt = sqlite_table_connection.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(sqlite_table_connection):
    orders = sqlite_table_connection.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1
    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_chek_all_data(sqlite_table_connection):
    users = sqlite_table_connection.get_all_data()
    print(users)
