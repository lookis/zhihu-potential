# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuProtentialItem(scrapy.Item):
    question_id = scrapy.Field()
    title = scrapy.Field()
    domain = scrapy.Field()
    created = scrapy.Field()
    updated_time = scrapy.Field()
    topics = scrapy.Field()
    new_pv = scrapy.Field()
    new_follow_num = scrapy.Field()
    new_answer_num = scrapy.Field()
    new_upvote_num = scrapy.Field()
    pv = scrapy.Field()
    follow_num = scrapy.Field()
    answer_num = scrapy.Field()
    upvote_num = scrapy.Field()
    score = scrapy.Field()
    crawl_time = scrapy.Field()
