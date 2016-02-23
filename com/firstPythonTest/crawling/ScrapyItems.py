'''
Created on 2016. 2. 22.

@author: leejinwon
'''
import scrapy

class scrapyItem(scrapy.Item):
    title = scrapy.Field()
    link  = scrapy.Field()
     