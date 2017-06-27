# -*- coding: utf-8 -*-
from decimal import Decimal

from scrapy.exceptions import DropItem

from deals.models import Company, Deal


class StoreItemPipeline(object):
    def process_item(self, item, spider):
        company = Company.objects.get(name__iexact=spider.company_name)
        discount = Decimal('0')
        old_price = item.pop('old_price')

        if old_price and item['price']:
            discount = (old_price - item['price']) / old_price

        deal, created = Deal.objects.get_or_create(company=company, url=item['url'])

        deal.discount = discount
        deal.price = item['price']
        deal.title = item['title']
        deal.description = item['description']
        deal.save()


class DuplicatesPipeline(object):

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        if item:
            if item['url'] in self.urls_seen:
                raise DropItem('Duplicate deail found: %s' % item)
            else:
                self.urls_seen.add(item['url'])
                return item
