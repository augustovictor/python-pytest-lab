import pytest

def test_should_match_this_name():
    assert 1 == 1

def test_shouldnt_match_this_name():
    assert 1 == 1

# pytest test_match_func_names.py -v -k '_match and not shouldnt'