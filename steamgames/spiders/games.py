import scrapy
from ..items import SteamgamesItem



# Spider-Class
class SteamGames(scrapy.Spider):
    name = 'allgames'
    allowed_domains = ['store.steampowered.com']
    start_urls = [
        'https://store.steampowered.com/search/?category1=998&supportedlang=english&ndl=1']
    base_url = 'https://store.steampowered.com/search/'

    page = 1

    # For-Infinite-Scroll
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    # To-Get-Str-Data-Of-Review
    def review_summary(self, review_summary):
        cleaned_summary = ''
        try:
            cleaned_summary = review_summary.split('<br>')[0]
        except:
            cleaned_summary = 'None'
        return cleaned_summary

    # To-Get-Numerical-Data-Of-Review
    def review_data(self, review_summary):
        cleaned_summary = ''
        try:
            cleaned_summary = review_summary.split('<br>')[1]
        except:
            cleaned_summary = 'None'
        return cleaned_summary

    # Clean-Discount-Data
    def clean_discount(self, discount):
        if discount:
            return discount.lstrip('-')
        return discount

    # Get-Clean-Original_price
    def get_original_price(self, original):
        original_price = ''
        game_with_discount = original.xpath(".//div[contains(@class, 'search_price discounted')]")
        if len(game_with_discount) > 0:
            original_price = game_with_discount.xpath(".//span/strike/text()").get()
        else:
            original_price = original.xpath("normalize-space(.//div[contains(@class, 'search_price')]/text())").get()

        return original_price

    # Get-Clean-Discounted-Price
    def discounted_price_clean(self, discounted_price):
        if discounted_price:
            return discounted_price.strip()
        return discounted_price

    def parse(self, response):

        steam_item = SteamgamesItem()
        # Extract the game titles from the current page
        games = response.xpath("//div[@id='search_resultsRows']/a")
        for game in games:
            steam_item['game_url'] = game.xpath(".//@href").get()
            steam_item['game_name'] = game.xpath(".//span[@class='title']/text()").get()
            steam_item['release_date'] = game.xpath(
                ".//div[@class='col search_released responsive_secondrow']/text()").get()
            steam_item['reviews_summary'] = self.review_summary(
                game.xpath(".//span[contains(@class, 'search_review_summary')]/@data-tooltip-html").get())
            steam_item['review_data'] = self.review_data(
                game.xpath(".//span[contains(@class, 'search_review_summary')]/@data-tooltip-html").get())
            steam_item['discount'] = self.clean_discount(
                game.xpath(".//div[contains(@class, 'search_discount')]/span/text()").get())
            steam_item['original_price'] = self.get_original_price(
                game.xpath(".//div[contains(@class, 'search_price_discount_combined')]"))
            steam_item['discounted_price'] = self.discounted_price_clean(
                game.xpath("(.//div[contains(@class, 'search_price discounted')]/text())[2]").get())
            yield steam_item

        # Check-If-There-Is-Next-Page-Available

        if self.page < 2000:  # How-Much-Pages-We-Want-To-Extract
            self.page += 1
            next_url = f"{self.base_url}?sort_by=_ASC&category1=998&supportedlang=english&page={self.page}"
            yield scrapy.Request(url=next_url, callback=self.parse)

