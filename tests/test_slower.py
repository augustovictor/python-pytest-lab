import pytest
import datetime
import time
import random

@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    # nodeid's can have colons
    # keys become filenames within .cache
    # replace colons with something filename save

    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if (last_duration is not None):
        error_string = 'test duration over 2x last duration'
        assert this_duration <= last_duration * 2, error_string
    
@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    # pytest tests/test_slower.py -q -cache-clear to clean previous cache
    # pytest tests/test_slower.py -q -tb=line to see tests results only
    # pytest tests/test_slower.py -q --cache-show to see cache
    time.sleep(random.random())