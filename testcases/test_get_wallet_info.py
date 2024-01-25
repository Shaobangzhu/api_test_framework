from common.common_requests import Requests

class TestApi:
    def test_get_wallet_info(self):
        login_data = {
            "user": "周杰伦",
            "password": "1234abcd!"
        }
        login_res = Requests().post("/api/user/login", json=login_data)
        token = login_res.json()["data"]["token"]
        headers = {"token": token}
        res = Requests(headers).post("/api/wallet/get_wallet_info")
        print(res.text)