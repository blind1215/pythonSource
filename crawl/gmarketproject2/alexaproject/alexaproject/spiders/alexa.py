import scrapy


class AlexaSpider(scrapy.Spider):
    name = 'alexa'
    allowed_domains = ['www.alexa.com/topsites']
    start_urls = ['http://www.alexa.com/topsites/']

    def parse(self, response):
        pass
