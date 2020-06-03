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
            title = each.xpath('h3').xpath("string(.)").extract()[0]
            link = each.xpath('h3/a/@href').extract()[0]
            size = each.xpath('p[@class="details-item tag"]/b/text()').extract()[0]
            #content.replace(u'\xa0', u'')

            item['title'] = title.strip()
            item['link'] = link.strip()
            item['size'] = size.strip()


            yield item

