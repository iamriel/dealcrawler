from scrapy.spiders import CrawlSpider

from ..items import (
    DealItem,
    DealLoader,
)


class DealSpider(CrawlSpider):

    title_xpath = ''
    description_xpath = ''
    price_xpath = ''
    old_price_xpath = ''

    def get_deal(self, response):
        loader = DealLoader(item=DealItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_xpath('title', self.title_xpath)
        loader.add_xpath('description', self.description_xpath)
        loader.add_xpath('price', self.price_xpath)
        loader.add_xpath('old_price', self.old_price_xpath)
        return loader.load_item()
