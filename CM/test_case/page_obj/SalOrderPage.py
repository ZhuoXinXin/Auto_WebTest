from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class SalOrder(Page):
    """
    订单页面
    """

    url = '/#/order/list_CM_busSaleOrder'
    login_username_loc = (By.NAME, 'username')
    login_password_loc = (By.NAME, 'password')
    login_button_loc = (By.XPATH, '//*[@id="app"]/div/form/button')
    error_loc = (By.CLASS_NAME, r'el-message__content')

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username='', password=''):
        """
        获取的用户密码登录
        """
        self.open('/#/login')
        # self.cm_login
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    # 定义统一错误提示
    def error(self):
        return self.find_element(*self.error_loc).text

    # 定义登录正确后URL
    def user_login_success(self):
        return self.get_url()
