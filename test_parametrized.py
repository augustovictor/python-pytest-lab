import pytest
from utils import add

@pytest.mark.parametrize('value_pairs',[
    (1, 3),
    (2, 2)
])
def test_add_numbers(value_pairs):
    assert add(*value_pairs) == sum(value_pairs)

@pytest.mark.parametrize('a, b', [
    (1, 2),
    (3, 9)
])
def test_add_more_numbers(a, b):
    assert add(a, b) == a + b

# To rerun a specific test node (identifier) for given test:
# pytest test_parametrized.py::test_add_more_numbers[1-2] -v

numbers_to_try = (
    (2, 2),
    (12, 90),
    (-1, -10),
    (5, -1)
)

numbers_to_try_identifiers = (
    'Pair 1: (2, 2)',
    'Pair 2: (12, 90)',
    'Pair 3: (-1, -10)',
    'Pair 4: (5, -1)'
)

@pytest.mark.parametrize('value_pairs', numbers_to_try, ids=numbers_to_try_identifiers) #ids is optional
def test_with_given_variable(value_pairs):
    assert add(*value_pairs) == sum(value_pairs)