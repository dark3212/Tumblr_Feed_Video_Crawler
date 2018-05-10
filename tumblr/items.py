# -*- coding: utf-8 -*-

import scrapy


class TumblrItem(scrapy.Item):
    file_url = scrapy.Field()
    file_path = scrapy.Field()
    file_type = scrapy.Field()


class videoItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    fan = scrapy.Field()


class picItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    group = scrapy.Field()
    fan = scrapy.Field()

