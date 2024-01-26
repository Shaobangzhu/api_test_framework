import pytest

from common.common_requests import Requests

class TestApi:
    @pytest.mark.flaky(reruns=5)
    def test_get_wallet_info(self, token):
        headers = {"token": token("william")}
        res = Requests(headers).post("/api/wallet/get_wallet_info")
        print(res.text)