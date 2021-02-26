import requests


class TestWeWorkIF:
    access_token = ""

    def setup(self):
        """
        获取token
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww5564213832a9cfb6&corpsecret=izZQMvJ2VCz_4SrCExUCdqcCVYImplr67cVUMRKgTN0"
        r = requests.get(url)
        # print(r.json()["access_token"])
        self.access_token = r.json()["access_token"]

    def test_get_member(self):
        """
        读取成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&userid=franky"
        r = requests.get(url)
        print(r.json())

    def test_update_member(self):
        """
        更新成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.access_token}"
        body = {"userid": "robin",
                "name": "Nino Robin",
                "department": [2],
                "position": "后台工程师",
                "mobile": "10000000001",
                "gender": "2",
                "email": "NinoRobin@gzdev.com"}
        r = requests.post(url, json=body)
        print(r.json())

    def test_create_member(self):
        """
        创建成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}"
        body = {"userid": "Kurohige",
                "name": "黑胡子",
                "department": [3],
                "position": "前端工程师",
                "mobile": "10000000008",
                "gender": "1",
                "email": "Kurohige@gzdev.com"}
        r = requests.post(url, json=body)
        print(r.json())

    def test_delete_member(self):
        """
        删除成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.access_token}&userid=syankusu"
        r = requests.get(url)
        print(r.json())
