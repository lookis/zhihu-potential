# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json
import os
from datetime import datetime

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZhihuProtentialPipeline:

    lines = []

    def open_spider(self, spider):
        if not os.path.exists(os.path.dirname('data/.ignore')):
            os.makedirs(os.path.dirname('data/.ignore'))
        self.file = open(
            'data/%s.json' %
            datetime.today().strftime('%Y-%m-%d-%H-%M-%S'),
            'w', encoding='utf-8')

    def close_spider(self, spider):
        json.dump(
            sorted(
                self.lines,
                key=lambda x: x['question_id']),
            self.file,
            ensure_ascii=False)
        self.file.close()

    def process_item(self, item, spider):
        self.lines.append(ItemAdapter(item).asdict())
        return item
