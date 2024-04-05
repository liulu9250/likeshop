import pytest
import requests

from utils.api_url import BASE_URL
from utils.my_utils import logger


class Test01Likeshop:
    def setup_class(self):
        self.base_url = BASE_URL
        self.rs = requests.Session()

    # 定义函数
    def login(self, account, password, client):
        data = {
            "account": account,
            "password": password,
            "client": client
        }
        result = self.rs.post(url=self.base_url + "/api/account/login", json=data)
        logger.info(result.text)
        # 获取result中的token，并声明成self变量
        token = result.json()["data"]["token"]
        self.headers = {
            "token": token
        }
        return result

    # 获取个人信息
    def getInfo(self):
        result = self.rs.get(url=self.base_url + "/api/user/info", headers=self.headers)
        logger.info(result.text)
        return result

    # 上传头像
    def upload(self, pic):
        s = open(file=pic, mode="rb")
        files = {
            "file": s
        }
        result = self.rs.post(url=self.base_url + "/api/file/formimage", headers=self.headers, files=files)
        logger.info(result.text)
        # 关闭流
        s.close()
        return result
        # 修改保存信息

    def updateUserInfo(self, nickname, sex):
        data = {
            "nickname": nickname,
            "sex": sex
        }
        result = self.rs.post(self.base_url + "/api/pc/changeUserInfo", headers=self.headers, data=data)
        logger.info(result.text)
        return result

    # 获取信息
    def test_01_getInfo(self):
        # 登录，获取token
        self.login("15715317583", "yhzy15715317583", 2)
        # 获取token
        result = self.getInfo()
        assert result.json()["code"] == 1
        assert result.json()["data"]["mobile"] == "15715317583"

    # 上传头像
    list = ["pic/f06.jpeg", "pic/f07.jpg"]

    @pytest.mark.parametrize("pic", list)
    def test_02_upload(self, pic):
        # 登录，获取token
        self.login("15715317583", "yhzy15715317583", 2)
        # 获取token
        result = self.upload(pic)
        assert result.json()["code"] == 1

    # 修改用户信息
    def test_03_update(self):
        # 登录，获取token
        self.login("15715317583", "yhzy15715317583", 2)
        # 获取token
        result = self.updateUserInfo("小王", 2)
        assert result.json()["code"] == 1
