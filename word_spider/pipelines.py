# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WordSpiderPipeline(object):
    handles = {}
    def process_item(self, item, spider):
        #print "saving to : ", spider.output_path
        if self.handles.has_key(spider.output_path):
            fo = self.handles[spider.output_path]
        else:
            fo = open(spider.output_path, "w+")
            self.handles[spider.output_path] = fo
        # item should be utf8 encoded.
        #fo.write(item['word'] + "\t" + item['category'] + "\n")
        fo.write(item.get_write_line())
        return item
