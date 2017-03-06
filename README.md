# new_word_spider_chn

中文新词爬虫

### 运行
```bash
scrapy crawl {爬虫名称}
```

#### 说明
可能需要配置代理:
```
# windows
set http_proxy=http://host:port
set https_proxy=http://host:port
#linux
export http_proxy=http://host:port
export https_proxy=http://host:port
```

### 当前可用爬虫
参见: `word_spider/spiders`。
包括:
```
- baidu-hotword: 百度热门新词
- baidu: 百度各排行榜
- star: 娱乐明星
```