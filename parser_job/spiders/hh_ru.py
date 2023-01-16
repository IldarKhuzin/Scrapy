# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

class HhRuSpider(scrapy.Spider):
    name = 'hh_ru'

    allowed_domains = ['hh.ru']
    start_urls = [
        'https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=data+scientist%2F&excluded_text=&professional_role=96&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20'
    ]

    def parse(self, response:HtmlResponse):

        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        vacansies_links = response.xpath('//a[@class="serp-item__title"]/@href')
        for link in vacansies_links:
            yield response.follow(link, callback=self.parse_vacansy)

        print(
            '\n#######################\n%s\n########################\n'%response.url
        )

    def parse_vacansy(self, response: HtmlResponse):
        print(
            '\n#*****************##\n%s\n#******************#\n' % response.url
        )