import pytest
import sqlite3
from models import Employee

@pytest.fixture
def ultimate_data():
    return 1000

@pytest.fixture
def db_employees():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    drop_table_employee = "DROP TABLE IF EXISTS employees"

    cursor.execute(drop_table_employee)

    create_table_query = """
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(80) NOT NULL,
            lastname VARCHAR(80) NOT NULL,
            pay DECIMAL(5,2)
        )
    """

    employees_to_insert = [
        (None, 'NameEmp1', 'LastnameEmp1', 300),
        (None, 'NameEmp1', 'LastnameEmp1', 500),
        (None, 'NameEmp2', 'LastnameEmp2', 370),
        (None, 'NameEmp3', 'LastnameEmp3', 320.90),
        (None, 'NameEmp4', 'LastnameEmp4', 8900.18),
        (None, 'NameEmp5', 'LastnameEmp5', 120),
    ]

    insert_employees_query = "INSERT INTO employees VALUES (?, ?, ?, ?)"
        
    cursor.execute(create_table_query)
    cursor.executemany(insert_employees_query, employees_to_insert)
    
    select_employees_query = 'SELECT * FROM employees'

    result = cursor.execute(select_employees_query)
    rows = result.fetchall()

    items = [Employee(*row) for row in rows]
    return items

@pytest.fixture(scope='session')
def setup_db():
    """Setup db"""
    yield

    """Teardown db"""