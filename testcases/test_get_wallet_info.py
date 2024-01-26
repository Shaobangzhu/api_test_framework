import pytest

from common.common_requests import Requests
from common.yaml_config import GetConf

class TestApi:
    @pytest.fixture()
    def token(self):
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

    def test_get_wallet_info(self, token):
        headers = {"token": token("william")}
        res = Requests(headers).post("/api/wallet/get_wallet_info")
        print(res.text)