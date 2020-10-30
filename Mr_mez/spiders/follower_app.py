# -*- coding: utf-8 -*-
import scrapy
from Mr_mez.items import MrMezItem
import xlrd


class FollowerAppSpider(scrapy.Spider):
    name = 'follower_app'
    start_urls = ['https://instagram.com']

    def convert_str_to_number(self, x):
        total_stars = 0
        num_map = {'k': 1000, 'm': 1000000, 'b': 1000000000}
        if x.isdigit():
            total_stars = int(x)
        else:
            if len(x) > 1:
                total_stars = float(x[:-1]) * num_map.get(x[-1], 1)
        return int(total_stars)

    def parse(self, response):
        wb = xlrd.open_workbook("IG_accounts.xls")
        sheet = wb.sheet_by_index(0)
        for i in range(sheet.nrows):
            url = sheet.cell_value(i, 0)
            yield response.follow(url, callback=self.parse_data)

    def parse_data(self, response):
        item = MrMezItem()
        info = response.xpath(
            "//meta[@name='description']/@content").extract_first()
        info_list = info.split(" ")
        follower_str = info_list[0]
        follower_str_wo = follower_str.replace(',', '')
        follower_int = self.convert_str_to_number(follower_str_wo)
        page_url = response.url
        usernamelist = page_url.split('/')
        item['url'] = page_url
        item['username'] = usernamelist[-2]
        item['follower'] = follower_int
        yield item
