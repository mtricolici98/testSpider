# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'biliard'
    start_urls = [
        'https://billiard.ru/catalog/bilyardnye_kii/',
    ]

    def parse(self, response):
        for product in response.css('div.list_item_wrapp'):
            yield {
                'text': product.css('div.list_item > div.description_wrapp > div.description > div.item-title > a > span::text').extract_first(),
                'link': response.urljoin(product.css('div.list_item > div.description_wrapp > div.description > div.item-title > a').attrib['href'])
            }

        next_page_url = response.css('#right_block_ajax > div.inner_wrapper > div.ajax_load.cur.list > div.bottom_nav.list > div.module-pagination > div > ul > li.flex-nav-next > a').attrib["href"]
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
