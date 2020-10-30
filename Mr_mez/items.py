# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MrMezItem(scrapy.Item):
    url = scrapy.Field()
    username = scrapy.Field()
    follower = scrapy.Field()
