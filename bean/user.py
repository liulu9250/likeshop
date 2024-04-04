from com.baidu.utils.api_url import BASE_URL
from com.baidu.utils.my_utils import logger


class User:
    def __init__(self, rs):
        self.rs = rs
        self.headers = {
            "X-Requested-With": "XMLHttpRequest"
        }
        self.base_url = BASE_URL

        # 声明成函数

    def login(self, username, password):
        data = {
            "account": username,
            "password": password,
            "code": "1234",
            "remember_account": "on"
        }
        result = self.rs.post(url=self.base_url + "/admin/account/login.html", data=data, headers=self.headers)
        logger.info(result.text)
        return result
