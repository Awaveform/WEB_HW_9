# WEB_HW_9

pip install lxml
pip install requests
pip install beautifulsoup4

# practical example

poetry add beautifulsoup4
poetry add requests
poetry add sqlalchemy
poetry add Scrapy

# scrappy

# in current dir
scrapy startproject test_spyder
# in created dir
scrapy genspider authors quotes.toscrape.com
# start some spider
scrapy crawl name_of_spider

# docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management
