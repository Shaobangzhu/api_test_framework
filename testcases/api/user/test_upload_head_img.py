from urllib3 import encode_multipart_formdata

from common.tools import sep, get_project_path
from common.common_requests import Requests
import allure

class TestApi:
    @allure.feature("product")
    @allure.story("upload_img")
    @allure.description("上传头像图片")
    def test_upload_img(self, token):
        img_path = get_project_path()+sep(["img","upload_file.jpg"], add_sep_before=True)
        file_data={"file":("upload_img", open(img_path, "rb").read())}
        encode_data = encode_multipart_formdata(file_data)
        data=encode_data[0]
        headers={"token":token("william"), "Content-Type":encode_data[1]}
        res=Requests(headers).post("/api/user/upload_head_img", data=data)
        print(res.text)
        assert res.json()["code"]==200
        assert res.json()["msg"]=="成功"