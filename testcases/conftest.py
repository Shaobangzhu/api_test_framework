import pytest

from common.common_requests import Requests
from common.yaml_config import GetConf

@pytest.fixture()
def token():
    def _token(user):
        username,password = GetConf().get_username_password(user)
        login_data = {
            "user": username,
            "password": password
        }
        login_res = Requests().post("/api/user/login", json=login_data)
        token = login_res.json()["data"]["token"]
        return token
    return _token