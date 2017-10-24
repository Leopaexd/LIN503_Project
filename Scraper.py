# Author: Oliver Glant
# Web scraper for swedish forum posts

import scrapy

class FlashbackSpider(scrapy.Spider):
    name = "FlashbackSpider"

    def start_requests(self):
       # yield scrapy.Request('https://www.flashback.org/t1570091',self.parse) #thread on cheese doodles
        yield scrapy.Request('https://www.flashback.org/f350', self.parse_threads) #candy, fruit and snacks subforum

    def parse_threads(self,response):
        for thread in response.css('td.td_title'):
            threadLink = thread.css('a::attr("href")').extract_first()
            #selector.xpath('//div/@href')
            yield response.follow(threadLink, self.parse)

    def parse(self, response):
        for post in response.css('div.post_message'):
            yield {
                'post': post.css('div.post_message::text').extract(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)