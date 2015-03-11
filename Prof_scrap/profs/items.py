# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProfsItem(scrapy.Item):
    # define the fields for your item here like:
    ids=scrapy.Field()
    name = scrapy.Field()
    dept = scrapy.Field()
    degn = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    pass
