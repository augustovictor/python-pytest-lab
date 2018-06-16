import pytest
import sqlite3
import json
from models import Employee
from models import unnecessary_math

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

@pytest.fixture(scope='session')
def author_file_json(tmpdir_factory):
    python_author_data = {
        'Author1': { 'city': 'Boston' },
        'Author2': { 'city': 'Portland' },
        'Author3': { 'city': 'Sao Paulo' }        
    }

    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file: {}'.format(str(file)))

    with file.open('w') as f:
        json.dump(python_author_data, f)
    
    return file

def pytest_addoption(parser):
    parser.addoption('--myopt', action='store_true', help='Some boolean option')
    parser.addoption('--foo', action='store', default='bar', help='foo: bar or baz')

@pytest.fixture(autouse=True)
def add_um(doctest_namespace):
    doctest_namespace['um'] = unnecessary_math