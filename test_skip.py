import pytest

@pytest.mark.skip(reason='Api is not well defined')
def test_skip_this():
    assert 1 == 2

@pytest.mark.skipif(1 == 2, reason='Just checkint skipif')
def test_marked_to_skip():
    assert 1 == 1