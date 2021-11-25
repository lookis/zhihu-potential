import re
from datetime import datetime

import scrapy

from ..items import ZhihuProtentialItem


class ZhihuPotentialSpider(scrapy.Spider):
    name = 'zhihu-potential'
    allowed_domains = ['zhihu.com']
    base_path = 'https://www.zhihu.com/api/v4'
    start_urls = [
        'https://www.zhihu.com/api/v4/creators/rank/potential?domain=%s&sort_type=all' % domain for domain in [0] + list(range(100001, 100030))]

    def process_item(self, item, domain):
        question = item['question']
        reaction = item['reaction']
        return ZhihuProtentialItem(
            question_id=question['id'],
            title=question['title'],
            domain=domain,
            created=question['created'],
            updated_time=question['updated_time'],
            topics=[topic['name'] for topic in question['topics']],
            new_pv=reaction['new_pv'],
            new_follow_num=reaction['new_follow_num'],
            new_answer_num=reaction['new_answer_num'],
            new_upvote_num=reaction['new_upvote_num'],
            pv=reaction['pv'],
            follow_num=reaction['follow_num'],
            answer_num=reaction['answer_num'],
            upvote_num=reaction['upvote_num'],
            score=reaction['score'],
            crawl_time=datetime.today().strftime('%Y/%m/%d %H:%M:%S'))

    def parse(self, response):
        domain = int(
            re.match(
                'domain=(\\d+)',
                response.url.split('?')[1]).group(1))
        for item in response.json()['data']:
            yield self.process_item(item, domain)
        if not response.json()['paging']['is_end']:
            yield self.base_path + response.json()['paging']['next']
