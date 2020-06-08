# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import CrawlSpider, Rule
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
from anjuke.items import AnjukeItem

class AnjukeSpider(CrawlSpider):
    name = 'anjuke'

    allowed_domains = ['anjuke.com']
    start_urls = ['https://wh.zu.anjuke.com/']
    pagelink = LinkExtractor(allow=("fangyuan\/p\d+"))
    rules = [

        Rule(pagelink,callback="parse_item",follow=True)
    ]

    def parse_item(self, response):
        for each in response.xpath('//div[@class="zu-info"]'):

            item = AnjukeItem()
            titleold = each.xpath('h3').xpath("string(.)").extract()[0]
            title = self.zhuanma(titleold)
            link = each.xpath('h3/a/@href').extract()[0]
            sizeold = each.xpath('p[@class="details-item tag"]/b/text()').extract()[0]
            size=self.zhuanma(sizeold)
            #content.replace(u'\xa0', u'')

            item['title'] = title.strip()
            item['link'] = link.strip()
            item['size'] = size.strip()


            yield item
    def zhuanma(self,mm):
        str1 = ''
        dicts = {'驋': '1', '餼': '2', '龤': '3', '麣': '4', '鑶': '5', '齤': '6', '鸺': '7', '閏': '8', '龥': '9', '龒': '0',
                 '.': '.'}
        for i in mm:
            if i in dicts:
                ss = dicts[i]
                str1 += ss
            else:
                str1 += i
        return str1

