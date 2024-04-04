import requests

from com.baidu.bean.brand import Brand
from com.baidu.bean.user import User


class TestLikeshop02:
    def setup_class(self):
        # 创建一个请求的会话对象
        self.rs = requests.Session()
        # 登录
        user = User(self.rs)
        user.login("admin", "admin")

    def test_brand_01(self):
        brand = Brand(self.rs)
        result = brand.addBrand("xxxxxx", "X", "uploads/images/2022021111014949ae08187.png", 1, 1, "xxx")
        assert result.json()["code"] == 1
