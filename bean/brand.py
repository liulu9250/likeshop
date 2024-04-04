from com.baidu.utils.api_url import BASE_URL
from com.baidu.utils.my_utils import logger


class Brand:
    def __init__(self, rs):
        self.rs = rs
        self.headers = {
            "X-Requested-With": "XMLHttpRequest"
        }
        self.base_url = BASE_URL

    def addBrand(self, name, initial, image, sort, is_show, remark):
        data = {
            "name": name,
            "initial": initial,
            "image": image,
            "sort": sort,
            "is_show": is_show,
            "remark": remark
        }
        result = self.rs.post(url=self.base_url + "/admin/goods_brand/add.html", data=data, headers=self.headers)
        # 打印日志
        logger.info(result.text)
        return result

    def selectBrand(self):
        pass

