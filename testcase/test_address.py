from api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    def test_create_member(self):
        self.address.delete_member("zoro")
        self.address.create_member(userid="zoro", name="Nonoroa Zoro", department=[1], mobile="18000000002", gender=1, email="Zoro@163.com")
        r = self.address.get_member("zoro")
        # 推荐使用get
        assert r.get("name", "not found") == "Nonoroa Zoro"
