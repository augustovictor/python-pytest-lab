import pytest
import utils
from utils import add

@pytest.mark.xfail(utils.__version__ < '0.2.0',
reason='Not supported until version 0.2.0')
def test_add():
    assert add(1,1) == 3
