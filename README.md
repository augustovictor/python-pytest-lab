# python-pytest-lab

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
- `--collect-only` shows what tests will run under given arguments;