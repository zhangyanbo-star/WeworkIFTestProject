from api.base import Base

"""
封装，提高复用性
"""


class Address(Base):

    def get_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        r = self.send('get', url)
        return r

    def update_member(self, userid, name, department: list, position, mobile, gender, email, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {"userid": userid,
                "name": name,
                "department": department,
                "position": position,
                "mobile": mobile,
                "gender": gender,
                "email": email}
        # 把kwargs更新到body中
        body.update(kwargs)
        r = self.send('post', url, json=body)
        # r = requests.post(url, json=body)
        return r

    def create_member(self, userid, name, department: list, mobile, gender, email, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {"userid": userid,
                "name": name,
                "department": department,
                "mobile": mobile,
                "gender": gender,
                "email": email}
        body.update(kwargs)
        r = self.send('post', url, json=body)
        # r = requests.post(url, json=body)
        return r

    def delete_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        r = self.send('get', url)
        # r = requests.get(url)
        return r
