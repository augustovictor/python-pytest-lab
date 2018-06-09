import pytest

@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture"""
    return 'This is a function scoped returned value'

@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture"""
    return 'This is a module scoped returned value'

@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture"""
    return 'This is a session scoped returned value'

@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture"""
    return 'This is a class scoped returned value'

def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures"""
    print(sess_scope)
    print(mod_scope)
    print(func_scope)

def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests"""
    print(sess_scope)
    print(mod_scope)
    print(func_scope)

@pytest.mark.usefixtures('class_scope')
class TestFixtures():
    def test_3(self):
        """Test using a class scope fixture"""
        # print(class_scope) # We do not have access to the returned value of class_scope since we're using usefixtures statement

    def test_4(self):
        """Again, multiple tests are more fun"""