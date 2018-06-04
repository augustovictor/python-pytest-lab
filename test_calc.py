import pytest
import time
import calc

@pytest.mark.basic_operation
def test_add():
    result = calc.add(1,1)
    assert result == 3

def test_slow():
    time.sleep(2)
    assert 1 == 1

@pytest.mark.skip
def test_fail():
    assert 1 == 2

@pytest.mark.xfail
def test_expected_to_fail():
    assert 1 == 3

@pytest.mark.skip
def test_skip_this_one():
    assert 1 == 4

def test_failing_test():
    assert 1 == 20

@pytest.mark.basic_operation
def test_basic():
    assert 2 == 2