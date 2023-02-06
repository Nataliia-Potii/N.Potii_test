import pytest


@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name('Sergii')

    assert user[0] == ('Maydan Nezalezhnosti 1', 'Kyiv', '3127', 'Ukraine')


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25
    

@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, 'печиво', 'солодке', 30)
    product_qnt = database.select_product_qnt_by_id(4)
    assert product_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equel to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0] == (1, 'Sergii', 'солодка вода', 'з цукром')
    