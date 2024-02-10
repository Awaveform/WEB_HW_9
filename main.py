from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.author import AuthorSpider
from spiders.quote import QuotesSpider

settings = get_project_settings()
configure_logging(settings)
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    try:
        yield runner.crawl(QuotesSpider)
        yield runner.crawl(AuthorSpider)
    except Exception as e:
        # Log the exception
        print(f"Error during crawling: {e}")
    finally:
        # Stop the reactor regardless of success or failure
        reactor.stop()


if __name__ == '__main__':
    crawl()
    reactor.run()
