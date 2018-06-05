import pytest
from utils import calc

@pytest.fixture(autouse=True)
def before_and_after_each_test():
    # Setup db for example
    print('starging db')

    yield

    # Teardown db
    print('Tearing db down')

def test_expected_raise():
    with pytest.raises(TypeError):
        calc.add('a', 1)

def test_expect_value_error_raise():
    with pytest.raises(ValueError) as excinfo:
        calc.genericCalc(1, 2, 'multiply')
        assert excinfo.value.args[0] == "The values must be either 'add' or 'sub'"