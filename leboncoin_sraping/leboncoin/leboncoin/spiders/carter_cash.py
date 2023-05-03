import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import subprocess

def run_spider():
    subprocess.run(["scrapy", "crawl", "carter", "-O", "carter-cash.csv"])


class ImmoSpider(CrawlSpider):
    name = "carter"
    allowed_domains = ["www.carter-cash.com"]
    # start_urls = ["https://www.carter-cash.com/pneus/205-55-r16"]
    
    # ###///////////   pour faire sous forme de dictionnaire ////////////////////////////
    
    largeur =  {155: 155, 165: 165, 175: 175, 185: 185, 195: 195, 205: 205, 215: 215, 225: 225, 235: 235, 245: 245}
    hauteur =  {40: 40, 45: 45, 50: 50, 55: 55, 60: 60, 65: 65, 70: 70}
    diametre = {13:13,14:14,15:15,16:16,17:17,18:18,19:19}

    start_urls = []
    for l in largeur.values():
        for h in hauteur.values():
            for d in diametre.values():
                url = f"https://www.carter-cash.com/pneus/{l}-{h}-r{d}"
                start_urls.append(url)
    
    # ###/////////// //////////////////////////// ////////////////////////////


    
    film_details = LinkExtractor(restrict_css='h2 > a')
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
        # ////// les fonction de netoyage ///////////////////////
        descriptif = response.xpath('//h1[@class="name"]/text()').get()
        note = response.xpath('//div[@class="product-name"]/div/div/span[1]/text()[1]')
        runflat = response.xpath('//div[@id="features"]/ul/li[11]/span[2]/text()')
        consommation = response.xpath('//div[@id="features"]/ul/li[3]/span[2]/text()').get()
        charge = response.xpath('//div[@id="features"]/ul/li[9]/span[2]/text()').get()
        vitesse = response.xpath('//div[@id="features"]/ul/li[10]/span[2]/text()').get()
        indice_pluie = response.xpath('//div[@id="features"]/ul/li[4]/span[2]/text()').get()

        item = {}
        item["prix"] = response.xpath('//div[@class="price-container "]/div/div[@class="main-price"]/span[1]/text()').get()
        item["url-produit"] = response.url

        item["info_generale"] = response.xpath('//h1/div/text()').get().strip()
        item["descriptif"] = ' '.join(descriptif.split()[1:])
        
        item["Saisonalite"] = response.xpath('//div[@id="features"]/ul/li[1]/span[2]/text()').get().strip()
        item["type_Véhicule"] = response.xpath('//div[@id="features"]/ul/li[2]/span[2]/text()').get().strip()
     # ////// 
        item["Consommation"] = consommation if consommation and consommation.isalpha() and ('a' <= consommation.lower() <= 'f') else "inconnue"
    # ////// 
        
        item["Indice_Pluie"] = indice_pluie if indice_pluie and indice_pluie.isalpha() and ('a' <= indice_pluie.lower() <= 'f') else "inconnue"

    # //////        
        item["Bruit"] = response.xpath('//div[@id="features"]/ul/li[5]/span[2]/text()').get()
        if item["Bruit"] and not item["Bruit"].endswith("db"):
            item["Bruit"] = "inconnue"
            
        url_parts = response.url.split("/")
        tire_dimensions = url_parts[-1].split("-")
        item["Largeur"] = tire_dimensions[0]
        item["Hauteur"] = tire_dimensions[1].split("r")[0]
        item["Diametre"] = tire_dimensions[1].split("r")[1]        
        
        if charge and charge.isnumeric() and 1 <= int(charge) <= 100:
            item["Charge"] = charge
        else:
            item["Charge"] = "inconnue"
    # ////// 
        
        if vitesse and vitesse.isalpha() and 'a' <= vitesse.lower() <= 'z':
            item["Vitesse"] = vitesse
        else:
            item["Vitesse"] = "inconnue"
       # //////      
            
        if runflat:
            item["Runflat"] = runflat.get()
        else:
            item["Runflat"] = "inconnue"     
            
        # //////         
        if note:
            note_text = note.get().split('/')[0]
            if "reconditionné" not in note_text:
                item["note"] = note_text
            else:
                item["note"] = "note inconnue"
        else:
            item["note"] = "note inconnue"


        return item
                    

        


run_spider()