'''
Just run the command:
scrapy crawl profs -o profs_file.csv 
'''

import scrapy
from profs.items import ProfsItem

class ProfsDetail(scrapy.Spider):
    name = "profs"
    allowed_domains = ["iitm.ac.in/content/people"]
    start_urls = ["https://www.iitm.ac.in/info/faculty"]

    def parse(self, response):
        id_no=1
        for each in response.xpath('//table[@class="sticky-enabled"]/tbody/tr'):
            Item = ProfsItem()
	    Item['ids'] = id_no
            Item['name'] = each.xpath('td/a/text()').extract()
            Item['dept'] = each.xpath('td[2]/text()').extract()
            Item['degn'] = each.xpath('td[3]/text()').extract()
            Item['phone'] = each.xpath('td[4]/text()').extract()
            Item['email'] = each.xpath('td[5]/text()').extract()
            id_no += 1
	    yield Item
			
