# python-pytest-lab

## Test structure

```python
# GIVEN a db with 3 tasks
# WHEN another task is added
tasks.add(Task('Another task'))

#THEN the count increases by 1
assert tasks.count() == 4

``` 

## Running tests
- In order to run a single test we console: `pytest test_calc.py::test_add`;
- Verbose mode: `pytest test_calc.py -v`;
- Pytest runs tests with the following naming structure:
    - test_file.py
        - TestClassName
            - test_method_name
- Run tests:
    - That have failed last time: `--lf`;
    - Failed ones first then the others: `--ff`;
    - Quiet verbosity: `-q`;
    - Traceback print mode: `--tb=[auto,long,short,line,native,no]`;
    - With given marker: `-m basic_operation`
    - Exit on first error: `-x`
    - Show local variables along with their values: `-l`;
    - Report the tests slower than N: `--durations=0.01`;
    - Show the reasons: `-rs`;
    - Where functions match given name: `-k _raises`
        - `-k _raises and not delete` not to run `test_delete_raises()`;
- `--collect-only` shows what tests will run under given arguments;
- We can set tests marked as `xfail` that passed as failed tests by setting a pytest.ini file with the `following:
```python
[pytest]
xfail_strict=true
```
- To see how test are setup we can use the following parameter: `--setup-show`
- To see where fixtures are defined we run our tests with the parameter `--fixtures`;
- `--cache-show` shows what's in cache;
- `--cache-clear` to clear the cache with info like 'last failed';
- `doctest-modules` to run docstring tests

### Fixtures

Fixtures are functions that run before our tests (or after). Which in pytest context we can assume that it allows the separation of 'getting ready for' and 'cleaning up after'

To see how fixtures are setup and teared down we use the following command: `--setup-show`;

`pytestconfig` is a shortcut to `request.config`, and sometimes referred as 'pytest config object'.

### Pytest options

We can pass arguments to pytest by the command line when running our tests through `def pytest_addoption(parser)`

### Dependencies

In order to install a dependency and add to `requirements.txt` file we run in the command line: `pip install <dependency> && pip freeze > requirements.txt`

### Cache

We can also pass the result of one test session to another by the use of the built in cache `fixture`.

### Capsys

Allows us to retrieve stdout and stderr from some code, and disables output capture temporarily.

### Monkeypatch

It is a dynamic modification of a class or module during runtime.

Functions provided by the built in fixture mokeypatch:
- `setatr(target, name, value=<notset>, raising=True)`: Set an attribute;
- `delattr(target, name=<notset>, raising=True)`: Delete an attribute;
- `setitem(dic, name, value)`: Set a dictionary entry;
- `delitem(dic, name, raising=True)`: Delete a dictionary entry;
- `setenv(name, value, prepend=None)`: Set an env variable;
- `delenv(name, value, raising=True`: Delete an env variable;
- `sysapth_prepend(path)`: Prepend path to `sys.path`, which is Python's list of import locations;
- `chdir(path)`: Change current working directory;

The `raising` parameter tells pytest whether or not to raise an exception if the item does not already exist.

The `prepend` parameter to `setenv` can be a character. If it is set, the value of the env variable will be changed to value + prepend + old value.

### doctest_namespace

Allows us to put code examples inside docstrings and test them.