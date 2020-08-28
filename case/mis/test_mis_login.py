"""
预置条件，交给初始化方法
步骤、测试数据、预期结果，交给测试方法
关闭浏览器，交给类级别的销毁方法
"""
# 0.定义测试类
import pytest

from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist

@pytest.mark.run(order=102)
class TestMisLogin:
    # 0.1 定义类级别的初始化方法
    def setup_class(self):
        # 1.打开浏览器
        self.driver = DriverUtils.get_mis_driver()
        # 创建业务方法所在的类的对象
        self.mis_Login_proxy = MisLoginProxy()

    # 定义方法级别的初始化，恢复原点
    def setup(self):
        print(1)
        self.driver.get("http://ttmis.research.itcast.cn/")

    # 定义测试方法
    def test_mis_login(self):
        # 2.定义测试数据
        username = "testid"
        password = "testpwd123"
        # 3.调用业务方法
        self.mis_Login_proxy.test_mis_login(username, password)
        # 4.执行断言
        assert is_element_exist(self.driver, "退出")

    # 5.关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
