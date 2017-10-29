# Author: Oliver Glant
# Web scraper for swedish forum posts

import scrapy


class FlashbackSpider(scrapy.Spider):
    name = "FlashbackSpider"

    def start_requests(self):
        # ONLY ONE OF THESE SHOULD BE UNCOMMENTED AT THE SAME TIME
        # yield scrapy.Request('https://www.flashback.org/f350', self.parse_threads) # Candy, fruit and snacks (1)
        # yield scrapy.Request('https://www.flashback.org/f54', self.parse_threads)  # Physics, math and technology(2)
        # yield scrapy.Request('https://www.flashback.org/f34', self.parse_threads)  # Nazism subforum (3)
        # yield scrapy.Request('https://www.flashback.org/f175', self.parse_threads)  # Pets subforum (4)
        # yield scrapy.Request('https://www.flashback.org/f242', self.parse_threads)  # Roleplaying and board games (5)
        # yield scrapy.Request('https://www.flashback.org/f279', self.parse_threads)  # Relationship advice (6)
        yield scrapy.Request('https://www.flashback.org/f13', self.parse_threads)  # Cannabis subforum (7)

    def parse_threads(self, response):
        for thread in response.css('td.td_title'):
            thread_link = thread.css('a::attr("href")').extract_first()
            yield response.follow(thread_link, self.parse)

    def parse(self, response):
        for post in response.css('div.post_message'):
            yield {'post': post.css('div.post_message::text').extract(), }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
