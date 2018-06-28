import pytest
from services import RemoteOp


def test_get_remote_op(mocker):
    RemoteOp = RemoteOp
    mocker.patch.object(RemoteOp, 'remote_op')
    RemoteOp.remote_op.get_remote_data.return_value = 10
    data = RemoteOp.RemoteOp().get_remote_data('test')
    assert data['id'] == 10
