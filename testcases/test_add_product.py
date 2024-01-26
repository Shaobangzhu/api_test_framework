import pytest

from common.common_requests import Requests

goods_info_list = [
    {
        "product_title": "接口自动化测试-autotest1",
        "product_stock": 1,
        "product_price": "6000",
        "product_status": 1,
        "product_desc": "接口自动化测试-autotest1",
        "product_img": [
            "http://122.51.42.138:9090/product/product_img/1706245291833bf5bf2a3-0a05-414e-b75c-dfe014da0da2"
        ]
    },
    {
        "product_title": "接口自动化测试-autotest2",
        "product_stock": 1,
        "product_price": "7000",
        "product_status": 1,
        "product_desc": "接口自动化测试-autotest2",
        "product_img": [
            "http://122.51.42.138:9090/product/product_img/1706245291833bf5bf2a3-0a05-414e-b75c-dfe014da0da2"
            ]
    }
]

class TestApi:
    @pytest.mark.parametrize("goods_info", goods_info_list)
    def test_add_product(self, token, goods_info):
        headers = {"token":token("william")}
        res=Requests(headers).post("/api/product/publish_product", json=goods_info)
        print(res.text)
        assert res.json()["code"] == 200
        assert res.json()["msg"] == "成功"