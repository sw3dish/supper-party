from supper_party.items import RecipeItem

import json
import scrapy


class BonAppetitSitemapSpider(scrapy.spiders.SitemapSpider):
    name = "bon-appetit-sitemap-spider"
    allowed_domains = ["bonappetit.com"]
    sitemap_urls = ["https://bonappetit.com/sitemap.xml"]

    sitemap_follow = [
        "https://www.bonappetit.com/sitemap.xml\?year=2020&month=10&week=2"
    ]

    sitemap_rules = [("/recipe", "parse_recipe")]

    def parse_recipe(self, response):
        schema_json = response.xpath(
            "//script[@type='application/ld+json']/text()"
        ).get()
        # recipe_schema = json.loads(
        #     schema_json.replace("\r", "\\r").replace("\t", "\\t")
        # )
        item = RecipeItem(url=response.url, json=schema_json)
        yield item
