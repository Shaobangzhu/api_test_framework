import allure
from common.common_requests import Requests

class TestApi:
    @allure.description("调用获取用户钱包信息接口")
    @allure.epic("主页")
    @allure.feature("用户信息")
    @allure.story("用户钱包信息")
    @allure.tag("余额")
    def test_get_wallet_info(self, token):
        with allure.step("登录"):
            headers = {"token": token("william")}
        with allure.step("调用获取用户钱包信息接口"):
            res = Requests(headers).post("/api/wallet/get_wallet_info")
            print(res.text)
        with allure.step("断言"):
            assert res.json()["code"] == 200
            assert res.json()["msg"] == "成功"