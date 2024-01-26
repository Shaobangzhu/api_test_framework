from common.yaml_config import GetConf
from common.common_requests import Requests

def login(user):
    username, password = GetConf().get_username_password(user)
    login_data = {
        "user": username,
        "password": password
    }
    login_res = Requests().post("/api/user/login", json=login_data)
    return login_res