from common.common_requests import Requests

class TestApi:
    def test_get_left_menu_info(self, token):
        headers = {"token": token}
        res = Requests(headers).get("/api/router/router_list")
        print(res.text)