import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ImmoSpider(CrawlSpider):
    name = "immo"
    allowed_domains = ["www.immotram.fr"]
    start_urls = ["https://www.immotram.fr/acheter-bien-immobilier-proche-tramway-lille.html"]
    
    film_details = LinkExtractor(restrict_css='.products_listing--list > a')
    rule_film_details = Rule(film_details,
                             callback='parse_item',
                             follow=False,
                             )
    rules = (rule_film_details,)

    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers={'User-Agent': self.user_agent})

    def parse_item(self, response):
        item = {}
        item["prix"] = response.xpath('//div[@class="bloc_product_head--desc_price"]/p[@class="title title_medium"]/text()').get()
        item["descriptif"] = response.xpath('//h2[@class="title title_small_alt"]/text()').get()
        item["ville"] = response.xpath('//p[@class="title title_medium"][1]/text()').get()
        item["type"] = response.xpath('//div[@class="bloc_product_content--desc"]/ul/li[1]/h3/text()').get()
        item["salle_de_bain"] = response.xpath('//div[@class="bloc_product_content--desc"]/ul/li[2]/h3/text()').get()        
        item["nbr_chambre"] = response.xpath('//div[@class="bloc_product_content--desc"]/ul/li[3]/h3/text()').get()
        item["parcelle_m2"] = response.xpath('//div[@class="bloc_product_content--desc"]/ul/li/p[1]/text()').get()        
        item["jardin"] = response.xpath('//div[@class="bloc_product_content--desc"]/ul/li[5]/p/text()').get()
        item["electricité"] = response.xpath('//div[@class="bloc_product_content--desc"]/ul/li[6]/h3/text()').get()        
        item["etat"] = response.xpath('//div[@class="bloc_product_content--desc"]/ul/li[7]/p/text()').get()
        item["terrasse"] = response.xpath('//div[@class="bloc_product_content--desc"]/ul/li[8]/p/text()').get()
        
        
        return item
