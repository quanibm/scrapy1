# -*- coding: utf-8 -*-
import re
import os
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from urllib import parse
# import urlparse python2 解析url
from scrapy.loader import ItemLoader
from ArticleSpider.items import JobBoleArticleItem, ArticleItemLoader
from ArticleSpider.utils.common import get_md5

chromePath = os.path.join(os.path.abspath("."), 'driver/chromedriver')
fireFoxPath = os.path.join(os.path.abspath("."), 'driver/geckodriver')
operaPath = os.path.join(os.path.abspath("."), 'driver/operadriver')

class JobboleSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com']
    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhihu.com",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    def __init__(self):
        self.n = 0

    def parse(self, response):
        # 解析列表中的所有文章url并交给scrapy下载并进行解析
        pass

    def parse_detail(self, response):

        # 通过itemLoader加载item
       pass


    def start_requests(self):
        from selenium import webdriver
        # browser = webdriver.Chrome(executable_path=chromePath)
        browser = webdriver.Firefox(executable_path=fireFoxPath)
        # browser = webdriver.Opera(executable_path=operaPath)
        browser.get("https://www.zhihu.com/signin")
        browser.find_element_by_css_selector(".Login-aboardPhone").click()
        browser.find_element_by_css_selector(".SignFlow-supportedCountriesSelect").click()
        browser.find_element_by_css_selector(".Select-option:first-child").click()
        browser.find_element_by_css_selector(".SignFlow-accountInput input").send_keys("09561333006")
        browser.find_element_by_css_selector(".SignFlow-password input").send_keys("20120...")
        browser.find_element_by_css_selector(".Button.SignFlow-submitButton.Button--primary.Button--blue").click()

        import time
        time.sleep(10)
        Cookies = browser.get_cookies()
        cookie_dict={}
        import pickle
        for cookie in Cookies:
            #写入文件
            f = open(os.path.join(os.path.abspath('.'),"cookies/zhihu/", cookie['name'] + '.zhihu'), 'wb')
            pickle.dump(cookie, f)
            f.close()
            cookie_dict[cookie['name']] = cookie['value']
        browser.close()
        return [scrapy.Request(url=self.start_urls[0], dont_filter=True, headers=self.headers, cookies=cookie_dict)]
        # browser.find_element_by_id()
        # t_selector = Selector(text=browser.page_source)
        # print(browser.page_source)