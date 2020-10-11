from supper_party.items import RecipeItem

import scrapy


class BonAppetitSitemapSpider(scrapy.spiders.SitemapSpider):
    name = "bon-appetit-sitemap-spider"
    allowed_domains = ["bonappetit.com"]
    sitemap_urls = ["https://bonappetit.com/sitemap.xml"]
    sitemap_rules = [("/recipe/", "parse_recipe")]

    def parse_recipe(self, response):
        schema_json = response.xpath(
            "//script[@type='application/ld+json']/text()"
        ).get()
        item = RecipeItem(url=response.url, json=schema_json)
        yield item
