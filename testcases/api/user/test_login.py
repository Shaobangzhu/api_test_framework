from common.common_requests import Requests

class TestApi:
    def test_login(self):
        data = {
            "user": "周杰伦",
            "password": "1234abcd!"
        }
        res = Requests().post("/api/user/login", json=data)
        print("token的值为: ", res.json()["data"]["token"])