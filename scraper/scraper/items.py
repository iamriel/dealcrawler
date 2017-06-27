# -*- coding: utf-8 -*-
import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import (
    Compose,
    Identity,
    Join,
    TakeFirst,
)

from .parsers import clean_price, whitespace_trimmer


class DealItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()


class DealLoader(ItemLoader):
    default_input_processor = Identity()
    default_output_processor = TakeFirst()

    title_out = Compose(Join(), whitespace_trimmer)
    description_out = Compose(Join(), whitespace_trimmer)
    price_out = Compose(TakeFirst(), clean_price)
    old_price_out = Compose(TakeFirst(), clean_price)
