'''
Created on 2016. 2. 22.

@author: leejinwon
'''
import scrapy

class ScrapySpiderTest(scrapy.Spider):
    name = "linkednest"
    allowed_domains = ["linkednest.net"]
    start_urls = [
       "http://linkednest.net/player/playerDetailView/jwlee"           
    ]
    
    def parse(self, response):
        for attr in response.xpath('//div'):
            className = attr.xpath('class/text()').extract()
            aTag = attr.xpath('a/text()').extract()
            
            print 'className is ', className, ', aTag is ', aTag