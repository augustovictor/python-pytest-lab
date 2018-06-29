import pytest
from services.RemoteOp import RemoteOp

def stub_fetch_data():
    return { 'id': 1 } 

def test_get_remote_op(mocker):
    mocker.patch.object(RemoteOp, 'fetch_data', return_value=stub_fetch_data())
    data = RemoteOp().fetch_data()
    assert data['id'] == 1
