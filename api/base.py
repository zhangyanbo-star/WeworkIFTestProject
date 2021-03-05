import requests


class Base:
    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww5564213832a9cfb6&corpsecret=izZQMvJ2VCz_4SrCExUCdqcCVYImplr67cVUMRKgTN0"
        r = requests.request('get', url).json()
        # 要先定义再使用
        # r = self.send('get', url)
        self.access_token = r["access_token"]
        # 声明一个session
        self.session = requests.session()
        # 把 token 放入 session
        self.session.params = {'access_token': self.access_token}

    def send(self, *args, **kwargs):
        """
        把底层第三方requests剥离出来
        :param args:
        :param kwargs:
        :return:
        """
        r = self.session.request(*args, **kwargs)
        return r.json()
