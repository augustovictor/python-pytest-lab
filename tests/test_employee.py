import pytest
from models import Employee

class TestEmployee():

    employees = [
        pytest.param(Employee('NameEmp1', 'LastnameEmp1', 100), id='Emp 1'),
        pytest.param(Employee('NameEmp2', 'LastnameEmp2', 450), id='Emp 2'),
        pytest.param(Employee('NameEmp3', 'LastnameEmp3', 3900), id='Emp 3'),
        pytest.param(Employee('NameEmp4', 'LastnameEmp4', 380), id='Emp 4')
    ]

    @pytest.mark.parametrize('employee', employees)
    def test_email(self, employee):
        assert employee.email == f'{employee.username}.{employee.lastname}@email.com'