# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
regex = r"\d+"

class ReservePipeline(object):
    def process_item(self, item, spider):
        point_str = item.get('point')
        match = re.match(regex,point_str)
        item['point']=match.group(0)

        return item
