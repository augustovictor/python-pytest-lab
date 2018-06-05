import pytest

@pytest.fixture
def some_data():
    return 42

@pytest.mark.xfail
def test_some_data(some_data):
    some_data += 10
    assert some_data == 42

def test_some_data_again(some_data):
    assert some_data == 42

# ultimate_data fixture is defined in conftest.py file
def test_ultimate_data(ultimate_data):
    assert ultimate_data == 1000

def test_load_employees(db_employees):
    emp = db_employees[0]
    assert emp.email == f'{emp.username}.{emp.lastname}@email.com'