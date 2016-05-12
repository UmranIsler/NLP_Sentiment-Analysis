import scrapy

from kitap.items import KitapItem
from .. import items
from scrapy import log, Request

class KitapSpider(scrapy.Spider):
    name = "eksisozluk"
    allowed_domains = ["eksisozluk.com"]
    start_urls = [
        "https://eksisozluk.com/kitapyurdu-com--116066"]

    def parse(self, response):
        base_url = 'https://eksisozluk.com/kitapyurdu-com--116066?p=%s'
        for i in range(1,79):
             yield Request(base_url % i, self.parse2)

    def parse2(self, response):
        item = KitapItem()
        for i in response.css('ul#entry-list li'):
            comment = i.css("div.content *::text").extract()
            if comment:
                item['comment'] = comment
                yield item
