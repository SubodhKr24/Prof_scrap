# Prof_scrap
Insti Professors Details.

Name of the Project spider : "profs"

6 Fields created as follows:
    ids=scrapy.Field()  
    name = scrapy.Field()   
    dept = scrapy.Field()   
    degn = scrapy.Field()   
    phone = scrapy.Field()  
    email = scrapy.Field()  

allowed_domains = ["iitm.ac.in/content/people"]  
start_urls = ["https://www.iitm.ac.in/info/faculty"]

The datas are contained within : table[@class="sticky-enabled"]/tbody/tr
as shown here:

<tr class="odd"><td class="active"><a href="/info/fac/amal">Amal Kanti</a></td><td>BT</td><td>ASP</td><td>4121</td><td>amal</td> </tr>

<tr class="even"><td class="active"><a href="/info/fac/amitk">Amit Kumar</a></td><td>AE</td><td>Prof</td><td>4019</td><td>amitk</td> </tr>

So extraction of data is done as follows:

Item['ids'] = id_no

Item['name'] = each.xpath('td/a/text()').extract()

Item['dept'] = each.xpath('td[2]/text()').extract()

Item['degn'] = each.xpath('td[3]/text()').extract()

Item['phone'] = each.xpath('td[4]/text()').extract()

Item['email'] = each.xpath('td[5]/text()').extract()

id_no += 1 ;Incrementing the id.
