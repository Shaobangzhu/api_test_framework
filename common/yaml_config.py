import yaml
from common.tools import get_project_path, sep

class GetConf:
    def __init__(self):
        project_path = get_project_path()
        with open(project_path+sep(["config","environment.yaml"], add_sep_before=True),"r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username_password(self):
        return self.env["username"], self.env["password"]

    def get_url(self):
        """
        target website url
        :return:
        """
        return self.env["url"]