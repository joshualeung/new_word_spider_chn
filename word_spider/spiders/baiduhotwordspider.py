# -*- coding: utf-8 -*-
import time
import scrapy
from bs4 import BeautifulSoup

from word_spider.items import BaiduWordItem


class BaiduHotWordSpider(scrapy.Spider):
    name = "baidu-hotword"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://top.baidu.com/buzz?b=396&fr=topindex"
    ]
    base_url = "http://top.baidu.com/"
    output_path = "download/%s.txt" % name

    def parse(self, response):
        category = "热词"
        keywords = response.xpath("//a[@class='list-title']/text()").extract()
        for k in keywords:
            item = BaiduWordItem()
            item['word'] = k.encode("utf8")
            item['category'] = category
            yield item