# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy_zhihu.items import UserItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
    start_user = 'nie-zi-chuan-98'

    def start_requests(self):
        yield scrapy.Request(url=self.user_url.format(user=self.start_user), callback=self.parse_user)
        # yield scrapy.Request(url=self.followees_url.format(user=self.start_user), callback=self.parse_followees)
        # yield scrapy.Request(url=self.followers_url.format(user=self.start_user), callback=self.parse_followers)

    def parse_user(self, response):
        result = json.loads(response.text)
        # print(result)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield scrapy.Request(url=self.followees_url.format(user=result.get('url_token')), callback=self.parse_followees)
        yield scrapy.Request(url=self.followers_url.format(user=result.get('url_token')), callback=self.parse_followers)

    def parse_followers(self, response):
        result = json.loads(response.text)
        if result.get('data'):
            for result in result.get('data'):
                yield scrapy.Request(url=self.user_url.format(user=result.get('url_token')), callback=self.parse_user)

        if result.get('paging') and result.get('paging').get('is_end') is False:
            next_url = result.get('paging').get('next')
            yield scrapy.Request(url=self.followers_url.format(user=next_url), callback=self.parse_followers)

    def parse_followees(self, response):
        result = json.loads(response.text)
        if result.get('data'):
            for result in result.get('data'):
                yield scrapy.Request(url=self.user_url.format(user=result.get('url_token')), callback=self.parse_user)

        if result.get('paging') and (result.get('paging').get('is_end') is False):
            next_url = result.get('paging').get('next')
            yield scrapy.Request(url=self.followees_url.format(user=next_url), callback=self.parse_followees)
