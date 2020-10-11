import json
import scrapy

from supper_party.items import RecipeItem
from supper_party.helpers import generate_issue_dates, make_absolute_url

BA_URL = "https://www.bonappetit.com/"


class BonAppetitSpider(scrapy.Spider):
    name = "bon-appetit"
    allowed_domains = ["www.bonappetit.com"]
    start_urls = [BA_URL]

    def parse(self, response):
        """
        Starts by parsing each issue landing page
        """
        # for (year, month) in generate_issue_dates():
        for (year, month) in [(2020, 10), (2020, 9)]:
            # We have to pad out the month to 2 digits
            url = "https://www.bonappetit.com/search?content=recipe&issueDate={}-{:02d}-01".format(
                year, month
            )
            yield scrapy.Request(url=url, callback=self.parse_issue_page)
            break

    def parse_issue_page(self, response):
        # get all the recipes on this page
        recipes = response.xpath("//a[@class='photo-link']")
        recipe_urls = [
            "https://www.bonappetit.com{}".format(href)
            for href in recipes.xpath(".//@href").extract()
        ]
        for url in recipe_urls:
            yield scrapy.Request(url=url, callback=self.parse_recipe)
            break

        # go to the next page using the link
        next_page = response.xpath("//a[@class='the-next-page']")
        next_page_url = next_page.xpath(".//@href").get()
        if next_page_url is not None:
            yield scrapy.Request(
                url=make_absolute_url(BA_URL, next_page_url),
                callback=self.parse_issue_page,
            )

    def parse_recipe(self, response):
        schema_json = response.xpath(
            "//script[@type='application/ld+json']/text()"
        ).get()
        recipe_schema = json.loads(
            schema_data.replace("\r", "\\r").replace("\t", "\\t")
        )
        item = RecipeItem(url=response.url, json=json)
        yield item
