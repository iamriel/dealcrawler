# -*- coding: utf-8 -*-

import os
import sys

from django.core.wsgi import get_wsgi_application

DIRNAME = os.path.abspath(os.path.dirname(__file__))
PROJECT_SRC_DIR = os.path.join(DIRNAME, '..', '..')

sys.path.append(PROJECT_SRC_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE', 'dealcrawler.settings'))
application = get_wsgi_application()

BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scraper.pipelines.DuplicatesPipeline': 300,
    'scraper.pipelines.StoreItemPipeline': 300,
}
