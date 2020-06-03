# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class AnjukePipeline(object):
    def __init__(self):
        self.filename = open("anjuke.json", "a", encoding="utf-8")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False)+ "," + "\n"
        # text = json.dumps(dict(item)) + "\n"
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.close()
