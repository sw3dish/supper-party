from supper_party.items import RecipeItem

import json
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
        schema_json = schema_json.replace("\n", "").replace("\t", "")
        schema_data = json.loads(schema_json)
        storage_json = json.dumps(schema_data, separators=(",", ":"))
        item = RecipeItem(
            url=response.url,
            title=schema_data["name"],
            description=schema_data["description"],
            author=schema_data["author"]["name"],
            date_published=schema_data["datePublished"],
            date_created=schema_data["dateCreated"],
            recipe_yield=schema_data["recipeYield"],
            ingredients=schema_data["recipeIngredient"],
            json=storage_json,
        )
        yield item
