# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 启动浏览器驱动
dr = webdriver.Chrome()
dr.get('http://192.168.199.150:8080')
dr.maximize_window()
# 登录
dr.find_element_by_name('username').send_keys('admin')
dr.find_element_by_name('password').send_keys('123456')
dr.find_element_by_xpath('//*[@id="app"]/div/form/button').click()


# 元素显示等待
def set_element_wait(method, text):
    element = WebDriverWait(dr, 5, 0.5).until(
        EC.presence_of_element_located((method, text))
    )
    return element


# 定位元素
def find_element(colId):
    """
    :param colId: 字段Id
    :return:  返回元素
    """
    set_element_wait(By.XPATH, '//label[@for="{0}"]/../div/div'.format(colId))
    element = dr.find_element_by_xpath('//label[@for="{0}"]/../div/div'.format(colId))
    return element


# 获取下拉选项
def get_dropdown_list(count):
    """
    :param count: 下拉选项中的第几行。最后一行：last()
    :return: 空
    """
    dropdown_list = dr.find_element_by_xpath(
        '//ul[@class="el-scrollbar__view el-select-dropdown__list" and last()]/li[{0}]'.format(count))
    return dropdown_list


# 创建订单
# 打开订单界面
set_element_wait(By.XPATH, '//span[text()="订单管理"]')
dr.find_element_by_xpath('//span[text()="订单管理"]').click()
time.sleep(1)
dr.find_element_by_xpath('//span[text()="订单中心"]').click()

# 新增订单
set_element_wait(By.XPATH, '//span[text()="新增"]')
dr.find_element_by_xpath('//span[text()="新增"]').click()
time.sleep(1)

# 经销商
find_element('DtbId').click()

# 选择经销商
time.sleep(1)
get_dropdown_list('last()').click()

# 是否开票为是
find_element('IsInvoice').click()

# 新增商品明细
set_element_wait(By.XPATH, '//span[text()="新增"]')
dr.find_element_by_xpath('//span[text()="新增"]').click()
time.sleep(1)

# 选择商品
find_element('IsInvoice').click()
get_dropdown_list('last()').click()

# 选择规格


