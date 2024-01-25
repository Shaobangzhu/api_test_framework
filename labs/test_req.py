import requests
from common.yaml_config import GetConf

# username, password = GetConf().get_username_password()
# url = GetConf().get_url()
# data={
#     "user":username,
#     "password":password
# }
# res=requests.post(url+"/api/user/login", json=data)
# print(res.text)
# print(type(res))

url = GetConf().get_url()
token="JWT eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0cmFkaW5nX3N5c3RlbSIsImlkIjoyNCwiaWF0IjoxNzA2MTQ0MjQ2LCJleHAiOjE3MDY3NDkwNDZ9.DCNQ6vFrYbDDpev7O6QfgdfxKlwvkBEzbhpSLcaTDpA"
headers={
    "token": token
}
res=requests.post(url+"/api/wallet/get_wallet_info", headers=headers)
print(res.text)