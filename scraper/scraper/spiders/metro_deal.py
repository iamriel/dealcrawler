from scrapy.spiders.crawl import Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

from .base import DealSpider


class MetroDealSpider(DealSpider):
    company_name = 'Metrodeal'
    name = 'metro_deal'
    allowed_domains = [
        'dealshelve.com',
    ]

    start_urls = [
        'http://api.dealshelve.com/philippines/?c=cebu&c=davao&c=iloilo-bacolod&c=metro-manila&s=metrodeal&sb=&d=2000'
    ]

    rules = (
        Rule(
            LxmlLinkExtractor(
                restrict_xpaths='//*[contains(text(), "Next")]'
            ),
            follow=True
        ),
        # Deals
        Rule(
            LxmlLinkExtractor(
                allow='/deal/[-\w]+',
                deny=(
                    '/deals/[-\w]+',
                )
            ),
            follow=False,
            callback='get_deal'
        ),
    )

    title_xpath = '//*[@class="deal_details_title"]/text()'
    description_xpath = '//h1[text()[contains(., "Highlights")]]/following-sibling::ul'
    price_xpath = '//div[@class="deal_details_price"]/text()'
    old_price_xpath = '//div[@class="deal_details_price"]/span/text()'
