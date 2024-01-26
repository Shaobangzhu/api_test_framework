import os
import pytest
import json

from common.login import login
from common.tools import sep, get_project_path

@pytest.fixture()
def token():
    def _token(user):
        # 判断存放token的目录是否存在, 如果不存在则自动创建
        token_json_dir = sep([get_project_path(), "token_dir"])
        if not os.path.exists(token_json_dir):
            os.mkdir(token_json_dir)
        # 用户user对应的token的json文件
        token_json_path = sep([token_json_dir, user+"_token.json"])
        if not os.path.exists(token_json_path):
            # 文件不存在, 调用登录接口, 并把token写入json文件
            print(f"{user}对应的token的json文件不存在, 调用登录接口")
            token=login(user).json()["data"]["token"]
            print(f"写入{user}对应的token的json文件")
            with open(token_json_path, "w+") as write_token:
                write_token.write(json.dumps({"token": token}))
            return token
        else:
            # 文件存在的话, 则取出token的值
            print(f"{user}对应的token的json文件已经存在, 读取json文件中的token")
            with open(token_json_path, "r") as token_info:
                token=json.loads(token_info.read())
                return token["token"]

    return _token