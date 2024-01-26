import requests
from common.yaml_config import GetConf

username, password = GetConf().get_username_password("jay")
url = GetConf().get_url()
data={
    "user":username,
    "password":password
}
res=requests.post(url+"/api/user/login", json=data)

print(res.status_code)
print(res.ok)
print(res.text)
print(res.json())
print(res.elapsed.total_seconds()*1000)
print(res.headers)
print(res.url)

# url = GetConf().get_url()
# token="JWT eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0cmFkaW5nX3N5c3RlbSIsImlkIjoyNCwiaWF0IjoxNzA2MTQ0MjQ2LCJleHAiOjE3MDY3NDkwNDZ9.DCNQ6vFrYbDDpev7O6QfgdfxKlwvkBEzbhpSLcaTDpA"
# headers={
#     "token": token
# }
# res=requests.post(url+"/api/wallet/get_wallet_info", headers=headers)
# print(res.text)

# url=GetConf().get_url()
# token="JWT eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0cmFkaW5nX3N5c3RlbSIsImlkIjoyNCwiaWF0IjoxNzA2MTQ0MjQ2LCJleHAiOjE3MDY3NDkwNDZ9.DCNQ6vFrYbDDpev7O6QfgdfxKlwvkBEzbhpSLcaTDpA"
# headers={
#     "token": token
# }
# res=requests.get(url+"/api/router/router_list/", headers=headers)
# print(res.text)