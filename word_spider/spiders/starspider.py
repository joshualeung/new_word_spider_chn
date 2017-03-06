# -*- coding: utf-8 -*-
import time
import scrapy
from bs4 import BeautifulSoup

from word_spider.items import BaiduWordItem


class StarSpider(scrapy.Spider):
    name = "star"
    allowed_domains = ["123fans.cn"]
    start_urls = [
        "https://123fans.cn/allstars.php"
    ]
    output_path = "download/%s.txt" % name

    def parse(self, response):
        category = "123fans"
        keywords = response.xpath("//div[@class='starlist']/p[@class='stars']/span/a/text()").extract()
        for k in keywords:
            item = BaiduWordItem()
            item['word'] = k.encode("utf8")
            item['category'] = category
            yield item