from time import sleep
import unittest, random, sys
sys.path.append('./models')
sys.path.append('./page_obj')
from CM.test_case.page_obj.loginPage import login
from CM.test_case.models import myunit, function


class loginTest(myunit.MyTest):
    """CM登录测试"""

    # 测试用户登录
    def user_login_verify(self, username='', password=''):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        """用户名、密码为空登录"""
        self.user_login_verify(username='', password='')
        po = login(self.driver)
        self.assertEqual(po.error(), '登录失败，请确认用户名密码是否正确！')
        function.insert_img(self.driver, 'user_pawd_empty.jpg')

    def test_login2(self):
        """用户名错误"""
        self.user_login_verify(username='1234123', password='1234567')
        po = login(self.driver)
        self.assertEqual(po.error(), '登录失败，请确认用户名密码是否正确！')
        function.insert_img(self.driver, 'user_err.jpg')

    def test_login3(self):
        """用户名正确，密码错误"""
        self.user_login_verify(username='admin', password='1234111')
        po = login(self.driver)
        self.assertEqual(po.error(), '登录失败，请确认用户名密码是否正确！')
        function.insert_img(self.driver, 'pawd_err.jpg')

    def test_login4(self):
        """用户名、密码正确"""
        self.user_login_verify(username='admin', password='123456')
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.get_url(), 'http://192.168.199.150:8080/#/dashboard')
        function.insert_img(self.driver, 'user_pawd_empty.jpg')


if __name__ == '__main__':
    unittest.main()
