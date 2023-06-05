# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamgamesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_url= scrapy.Field()
    game_name= scrapy.Field()
    release_date= scrapy.Field()
    reviews_summary= scrapy.Field()
    review_data= scrapy.Field()
    discount = scrapy.Field()
    original_price= scrapy.Field()
    discounted_price= scrapy.Field()
