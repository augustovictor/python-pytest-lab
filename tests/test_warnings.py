import pytest
import warnings

def lame_function():
    warnings.warn('Please stop using this function', DeprecationWarning)
    # rest of function

def test_lame_function(recwarn):
    lame_function()
    assert len(recwarn) == 1
    w = recwarn.pop()

    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this function'

def test_lame_function_2():
    with pytest.warns(None) as warning_list:
        lame_function()

        assert len(warning_list) == 1
        w = warning_list.pop()
        assert w.category == DeprecationWarning
        assert str(w.message) == 'Please stop using this function'