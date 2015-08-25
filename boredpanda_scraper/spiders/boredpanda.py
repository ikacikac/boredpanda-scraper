# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http.request import Request
from datetime import datetime

from boredpanda_scraper.items import BoredpandaScraperItem, BoredpandaScraperItemLoader


class BoredpandaSpider(CrawlSpider):
    name = 'boredpanda'
    allowed_domains = ['boredpanda.com']
    # start_urls = ['http://www.boredpanda.com/']

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths=['//article/h2/a[@class="title"]']),
    #          callback='parse_item',
    #          follow=True),
    # )

    def start_requests(self):
        # yield Request('http://www.boredpanda.com/shiba-inu-stuck-in-bush-japan/',
        #                callback=self.parse_item)

        yield Request('http://www.boredpanda.com/model-tearing-herself-apart-grotesque-body-painting-jeampiere-dinamarca-poque/',
                       callback=self.parse_item)

    def parse_item(self, response):
        l = BoredpandaScraperItemLoader(item=BoredpandaScraperItem(),
                                        response=response)
        l.add_value('date_created', datetime.utcnow())
        l.add_xpath('title', '//h1[contains(@class, "post-title")]/'
                             'a[contains(@class, "title")]/text()')
        l.add_xpath('content', '//div[contains(@class, "post-content")]/'
                               'p[@style="text-align: justify;"]/text()')
        l.add_xpath('image_urls', '//div[contains(@class, "post-content")]/'
                                  'descendant::img/@src')
        l.add_xpath('votes', '//footer//div[@class="points"]/@data-points')
        l.add_value('url', response.url)
        return l.load_item()
