# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from boredpanda_scraper.items import BoredpandaScraperItem


class BoredpandaSpider(CrawlSpider):
    name = 'boredpanda'
    allowed_domains = ['boredpanda.com']
    start_urls = ['http://www.boredpanda.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = BoredpandaScraperItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
