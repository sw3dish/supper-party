# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()
    date_published = scrapy.Field()
    date_created = scrapy.Field()
    recipe_yield = scrapy.Field()
    ingredients = scrapy.Field()
    json = scrapy.Field()
