# coding = utf-8
# author = 王瑞

import json
from selenium import webdriver
import time
import random
import xlwt
import xlrd
import requests


class Wu8Tc(object):

    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('https://passport.58.com/login/')
        driver.find_element_by_xpath('//div[@class="mask_body_item change_login"]/span[1]').click()
        driver.find_element_by_xpath('//div[@class="mask_body_item"]/input[@id="mask_body_item_username"]').send_keys(
            '17310381334')
        driver.find_element_by_xpath(
            '//div[@class="mask_body_item"]/input[@id="mask_body_item_newpassword"]').send_keys('scb60242673.')
        driver.find_element_by_xpath('//button[@id="mask_body_item_login"]').click()
        time.sleep(15)
        cookie = driver.get_cookies()
        jsonCookie = json.dumps(cookie)
        with open('qqhomepage.json', 'w') as f:
            f.write(jsonCookie)
        with open('qqhomepage.json', 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())
        cookie = [item["name"] + "=" + item["value"] for item in listCookies]
        cookiestr = '; '.join(item for item in cookie)
        print(cookiestr)
        driver.close()
        self.start_url = 'https://info.vip.58.com/info/v1/list?id=1001&type=1001&pageIndex=2&pageSize=50'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'cookie': cookiestr}
        self.value = []
        self.value1 = []

    def run(self):
        # 解析url地址，获取url地址信息，此网页只用保存一次，不用循环，
        # json 数据，直接获取json，需要登录验证COOKIE，使用google插件自动化获取，保存格式以excel形式保存,设置爬取时间和UA伪装。
        html = requests.get(self.start_url, headers=self.headers).content.decode('utf-8')
        print(html)
        html = json.loads(html)
        listdata = html.get('info').get('listData')
        for li in listdata:
            self.value.append(li.get('title'))
            self.value1.append(li.get('url'))
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        a = ['标题', 'url地址']
        for i in range(0, 1):
            for j in range(2):
                sheet.write(i, j, a[j])  # 行 列 数据
        length = len(self.value1)
        for i in range(0, length):
            sheet.write(i + 1, 0, self.value[i])
            sheet.write(i + 1, 1, self.value1[i])

        # date = datetime.datetime.now()
        # time_name = date.strftime('%Y%m%d%H')
        # time_name = date.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}'.format(y='年', m='月', d='日', h='时', M='分', s='秒'))
        time_name = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
        # print(time_name)
        book.save(time_name + '数据.xls')
        print('保存成功')
        # print(len(self.value))
        # print(self.value1)


if __name__ == '__main__':
    w = Wu8Tc()
    w.run()
