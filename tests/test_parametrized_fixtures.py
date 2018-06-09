import pytest

mock_tasks = (
    (1, 'Task 1', 'Task desc'),
    (2, 'Task 2', 'Task desc'),
    (3, 'Task 3', 'Task desc'),
    (4, 'Task 4', 'Task desc')
)

@pytest.fixture(params=mock_tasks)
def task(request):
    # request is a built in fixture that represents the calling state of the fixture
    # it has a field param that is filled in with one element from the list assined to params attribute
    return request.param

def test_id_is_integer(task):
    assert isinstance(task[0], int)