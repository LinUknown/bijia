# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JDStockItem(scrapy.Item):
    uid = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    comments = scrapy.Field()
    create_time = scrapy.Field()
    changed = scrapy.Field()
    degree = scrapy.Field()
    predict_price = scrapy.Field()
    ###
    last_price = scrapy.Field()
    last_mobile_price = scrapy.Field()
    last_update = scrapy.Field()

class JDStockPrice(scrapy.Item):
    uid = scrapy.Field()
    price = scrapy.Field()
    mobile_price = scrapy.Field()
    timestamp = scrapy.Field()

class JDStockImage(scrapy.Item):
    uid = scrapy.Field()
    data = scrapy.Field()

class JDStockMobilePrice(scrapy.Item):
    uid = scrapy.Field()
    mobile_price = scrapy.Field()
    timestamp = scrapy.Field()

class JDStockPromotion(scrapy.Item):
    type = scrapy.Field()
    rebate = scrapy.Field()

    needMoney = scrapy.Field()
    reward = scrapy.Field()

class JDStockPromotionList(scrapy.Item):
    uid = scrapy.Field()
    promotionList = scrapy.Field()
