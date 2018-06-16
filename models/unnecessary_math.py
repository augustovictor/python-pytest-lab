def multiply(a, b):
    """
    Returns a multiplied by b
    'um' stands for unnecessary_math which is a fixture defined in conftest

    >>> um.multiply(4,3)
    12
    >>> um.multiply('a', 3)
    'aaa'
    """
    return a * b