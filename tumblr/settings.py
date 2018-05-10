# -*- coding: utf-8 -*-

BOT_NAME = 'tumblr'
SPIDER_MODULES = ['tumblr.spiders']
NEWSPIDER_MODULE = 'tumblr.spiders'
ROBOTSTXT_OBEY = False


FILES_STORE = './data/'
FILES_EXPIRES = 90
FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOADER_MIDDLEWARES = {
    'tumblr.middlewares.TumblrspiderSpiderMiddleware': 543,
}

ITEM_PIPELINES = {
    'tumblr.pipelines.TumblrspiderPipeline': 2,
#    'tumblrSpider.pipelines.MyFilesPipeline': 1,
}

