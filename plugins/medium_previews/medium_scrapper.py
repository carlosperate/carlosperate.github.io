#!/usr/bin/env python
"""
Retrieves Medium articles using Scrapy
"""
import scrapy
from scrapy.crawler import CrawlerProcess


MEDIUM_URL = ''
JSON_ESCAPE_STR = '])}while(1);</x>'


class MediumItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nameOfAuthor = scrapy.Field()
    linkOfAuthorProfile = scrapy.Field()
    article = scrapy.Field()
    articleLink = scrapy.Field()
    postingTime = scrapy.Field()
    recommendation = scrapy.Field()


class MediumPost(scrapy.Spider):
    name = 'medium_scrapper'
    handle_httpstatus_list = [401, 400]
    autothrottle_enabled = True

    def start_requests(self):
        start_urls = [MEDIUM_URL]
        for url in start_urls:
            yield scrapy.Request(url, method='GET', callback=self.parse)

    def parse(self,response):
        response_data = response.text
        print('\n\n\nRESPONSE TEXT START\n\n\n')
        print(response_data)
        print('\n\n\nRESPONSE TEXT END\n\n\n')
        for story in response.css('div.postArticle'):
            post_dict = {
                'nameOfAuthor': story.css('div.u-marginBottom10 div div.postMetaInline-authorLockup a::text').extract_first(),
                'linkOfAuthorProfile': story.css('div.u-marginBottom10 div div.postMetaInline-avatar a::attr(href)').extract_first(),
                'article': story.css('div.postArticle-content section div.section-content div h3::text').extract_first(),
                'articleLink': story.css('div.postArticle-readMore a::attr(href)').extract_first(),
                'postingTime': story.css('div div.u-marginBottom10 div div.postMetaInline-authorLockup div a time::text').extract_first(),
                'recommendation': story.css('div.u-paddingTop10 div.u-floatLeft div div button.u-disablePointerEvents::text').extract_first(),
            }
            print('\n\nPOST START\n\n')
            print(post_dict)
            print('\n\nPOST END\n\n')
            yield post_dict

        #response_split = response_data.split(JSON_ESCAPE_STR)
        #response_data = response_split[1]
        #filename = "medium.json"
        #writeTofile(filename, response_data)
        #print(response_data)
        
        #with codecs.open(filename,'r','utf-8') as infile:
        #    data=json.load(infile)
        #Check if there is a next tag in json data
        """
        if 'paging' in data['payload']:
            data=data['payload']['paging']
            if 'next' in data:
                #Make a post request
                print "In Paging, Next Loop"
                data=data['next']
                formdata={
                        'ignoredIds':data['ignoredIds'],
                        'page':data['page'],
                        'pageSize':data['pageSize']
                        }               
                yield scrapy.Request('https://www.medium.com/search/posts?q=Data%20Science',method='POST',body=json.dumps(formdata),headers=header,cookies=cookie,callback=self.parse)
        """

def scrapped_medium(username):
    MEDIUM_URL = 'https://www.medium.com/@{}/latest'.format(username)
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(MediumPost)
    process.start()

