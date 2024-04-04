import pytest
import requests


class TestLikeshop:
    # 初始化
    def setup_class(self):
        self.base_url = "http://localhost:6688"
        # 创建一个请求的会话对象
        self.rs = requests.Session()
        self.headers = {
            "X-Requested-With": "XMLHttpRequest"
        }
        # 调用登录的函数
        self.login("admin", "admin")

    @classmethod
    # 声明成函数
    def login(self, username, password):
        data = {
            "account": username,
            "password": password,
            "code": "1234",
            "remember_account": "on"
        }
        result = self.rs.post(url=self.base_url + "/admin/account/login.html", data=data, headers=self.headers)
        return result

    def getList(self, cate, type, page_no, page_size):
        data = {
            "cate": cate,
            "type": type,
            "page_no": page_no,
            "page_size": page_size
        }
        result = self.rs.get(url=self.base_url + "/admin/file/lists.html", params=data, headers=self.headers)
        print(result.text)
        return result

    def uploadFile(self, file, cate):
        data = {
            "cate": cate
        }
        # 文件参数
        s = open(file=file, mode="rb")
        files = {"file": s}
        result = self.rs.post(url=self.base_url + "/admin/file/image.html", data=data, files=files,
                              headers=self.headers)
        # 关闭流
        s.close()
        print(result.text)
        return result

    # get请求
    # 参数:params
    # 请求头:headers
    def test_01(self):
        result = self.getList("1", 1, 1, 10)
        assert result.json()["code"] == 1

    @pytest.mark.skip()
    # post请求
    # 参数:普通参数用data，json格式用json
    # 请求头:headers
    def test_02(self):
        result = self.login("admin", "admin")
        assert result.json()["msg"] == "登录成功"

    def test_03(self):
        result = self.uploadFile("D:\\pic\\photos1.jpg", 6)
        assert result.json()["code"] == 1
        print(result.status_code)
        print(result.headers)
