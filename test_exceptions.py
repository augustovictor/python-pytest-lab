import pytest
import calc

def test_expected_raise():
    with pytest.raises(TypeError):
        calc.add('a', 1)

def test_expect_value_error_raise():
    with pytest.raises(ValueError) as excinfo:
        calc.genericCalc(1, 2, 'sum')
        assert excinfo.value.args[0] == "The values must be either 'add' or 'sub'"