# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

class AnjukePipeline(object):
    def __init__(self):
        db='fangyuan'
        host='localhost'
        port=3306
        user='root'
        # 由于安全起见 对数据库密码进行了加密 这里配置自己的数据库即可 （原版十分中其实已经包含 这里防君子不防小人）
        passwd='638816zxz'
        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()
        #self.filename = open("anjuke.json", "a", encoding="utf-8")

    def process_item(self, item, spider):
        #values = (item['title'],item['link'],item['size'])
        sql="INSERT INTO anjuke(title,link,size) VALUES(%s,%s,%s)"
        self.db_cur.execute(sql,(item['title'],item['link'],item['size']))
        self.db_conn.commit()
        #text = json.dumps(dict(item), ensure_ascii=False)+ "," + "\n"
        # text = json.dumps(dict(item)) + "\n"
        #self.filename.write(text)
        return item

    def close_spider(self, spider):
        #self.filename.close()
        self.db_cur.close()
        self.db_conn.close()
