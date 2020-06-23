# coding = utf-8
# author = 王瑞

import requests
from lxml import etree
import time


# 设置爬取地址和下一页地址，添加UA，进入详细页，爬取内容

class SpiderIP(object):

    def __init__(self):
        self.start_url = 'https://www.kuaidaili.com/free/inha/1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        self.content = []

    def parse(self):
        html = requests.get(self.start_url, headers=self.headers)
        response = etree.HTML(html.content.decode())
        list_ip = response.xpath('//div[@id="list"]//tbody/tr')
        for li in list_ip:
            ip_dir = {}
            ip_dir['IP'] = li.xpath('/td[1]')
            print(ip_dir)


S = SpiderIP()
S.parse()
