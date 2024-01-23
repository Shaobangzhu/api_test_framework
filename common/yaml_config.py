import yaml

class GetConf:
    def __init__(self):
        with open("C:/Projects/api_test_framework/config/environment.yaml","r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_username_password(self):
        return self.env["username"], self.env["password"]

if __name__ == '__main__':
    # print(GetConf().get_username_password())
    GetConf()