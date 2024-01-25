import json

data = '{"user": "周杰伦", "password": "1234abcd!"}'
print(data)
print(type(data))

print("================= From String to JSON =================")

# str -> json
json_data = json.loads(data)
print(json_data)
print(type(json_data))

print("================= From JSON to String =================")

# json -> str
str_data = json.dumps(json_data, ensure_ascii=False)
print(str_data)
print(type(str_data))
