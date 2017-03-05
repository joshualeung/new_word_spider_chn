# -*- coding: utf-8 -*-
import time
import scrapy
from bs4 import BeautifulSoup

from word_spider.items import BaiduWordItem


class BaiduWordSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_pages = {
        "movie": "http://top.baidu.com/category?c=1&fr=topbuzz_b618",
        "tv": "http://top.baidu.com/category?c=2&fr=topbuzz_b659_c1",
        "varity": "http://top.baidu.com/category?c=3&fr=topcategory_c2",
        "cartoon": "http://top.baidu.com/category?c=5&fr=topcategory_c3",
        "noval": "http://top.baidu.com/category?c=10&fr=topcategory_c5"
    }
    start_urls = start_pages.values()
    base_url = "http://top.baidu.com/"
    output_path = "download/%s.txt" % name

    def parse(self, response):
        for url in self.get_sidebar_urls(response):
            yield scrapy.Request(url, callback=self.parse_detailed_rank)

        category = self.get_category(response)
        keywords = response.xpath("//div[@class='item-hd']/a[1]/@title").extract()
        for k in keywords:
            item = BaiduWordItem()
            item['word'] = k.encode("utf8")
            item['category'] = category.encode("utf8")
            #print "crawling: ", k.encode("gbk")
            yield item

    def parse_detailed_rank(self, response):
        print "parse detailed page: ", response.url
        category = self.get_category(response)
        keywords = response.xpath("//a[@class='list-title']/text()").extract()
        for k in keywords:
            item = BaiduWordItem()
            item['word'] = k.encode("utf8")
            item['category'] = category.encode("utf8")
            yield item

    def get_sidebar_urls(self, response):
        dead_link = "javascript:void(0)"
        sidebar_urls = response.xpath("//div[@class='hblock']/ul/li/a/@href").extract()
        result = []
        for url in sidebar_urls:
            url = url.strip()
            if dead_link == url:
                continue
            if not url.startswith("http"):
                url = self.base_url + url
            result.append(url)
        return result

    def get_category(self, response):
        category = response.xpath("//div[@class='hblock']/ul/li/a[contains(@class, 'se')]/@title").extract()
        if len(category) == 0:
            return ""
        return category[0]