# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.item


class OtodomscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ListingItem(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()
    price_per_m2 = scrapy.Field()
    # estimated_loan_installment = scrapy.Field()
    area = scrapy.Field()
    form_of_ownership = scrapy.Field()
    rooms = scrapy.Field()
    finish_condition = scrapy.Field()
    floor = scrapy.Field()
    balcony_garden = scrapy.Field()
    rent = scrapy.Field()
    parking_space = scrapy.Field()
    listing_description = scrapy.Field()
    # advert_details = scrapy.Field()
    # additional_info = scrapy.Field()