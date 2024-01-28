import scrapy
from scrapy.crawler import CrawlerProcess


# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     allowed_domains = ['quotes.toscrape.com']
#     start_urls = ['http://quotes.toscrape.com/']
#     custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "qoutes.json"}
#     urls = []  # test urls
#
#     def parse(self, response, **kwargs):
#
#         for quote in response.xpath("/html//div[@class='quote']"):
#             self.urls.append(quote.xpath("//a[contains(@href, 'author')]/@href").get())  # send link part to second spider
#             yield {
#                 "tags": quote.xpath(
#                     "div[@class='tags']/a/text()").extract(),
#                 "author": quote.xpath("span/small/text()").extract_first(),
#                 "quote": quote.xpath(
#                     "span[@class='text']/text()").extract_first(),  # .encode("ascii", "ignore").decode()
#             }
#         next_link = response.xpath("//li[@class='next']/a/@href").get()
#         if next_link:
#             yield scrapy.Request(url=self.start_urls[0] + next_link)
#         print(self.urls)
#
#
# # run spider QuotesSpider
# process = CrawlerProcess()
# process.crawl(QuotesSpider)
# process.start()


class AuthorSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json"}
    ind = 0  # test
    urls = ['author/Albert-Einstein', '/author/Marilyn-Monroe']  # test urls

    def parse(self, response, **kwargs):

        if self.ind < 2:
            next_link = self.start_urls[0] + self.urls[self.ind]
            yield scrapy.Request(url=next_link)

        for author in response.xpath("/html//div[@class='author-details']"):
            yield {
                "fullname": author.xpath("h3/text()").extract_first(),
                "born_date": author.xpath(
                    "//span[@class='author-born-date']/text()")
                .extract_first(),
                "born_location": author.xpath(
                    "//span[@class='author-born-location']/text()")
                .extract_first(),
                "description": author.xpath(
                    "//div[@class='author-description']/text()")
                .extract_first().strip(),
            }
        self.ind += 1


# run spider QuotesSpider
process = CrawlerProcess()
process.crawl(AuthorSpider)
process.start()
