from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from deputies.items import DeputiesItem

class DeputiesSpider(BaseSpider):
    name = "deputies"
    allowed_domains = ["camara.gov.br"]
    start_urls = [
    	"http://www.camara.gov.br/internet/deputado/Dep_Lista_foto.asp?Legislatura=54&Partido=QQ&SX=QQ&Todos=None&UF=QQ&condic=QQ&forma=lista&nome=&ordem=nome&origem=None"
    ]

    def parse(self, response):
    	hxs = HtmlXPathSelector(response)
    	deputies = hxs.select('//table[@class="cor"]//td')
    	items = []
    	for deputy in deputies:
    		item = DeputiesItem()
    		item['nome'] = deputy.select('.//b/text()').extract()[0].str()
    		item['img'] = deputy.select('.//img/@src').extract()
    		item['url'] = 'http://camara.gov.br/internet/deputado/' + deputy.select('.//a/@href').extract()[0]
    		item['email'] = deputy.select('.//a[contains(@href, "mailto")]/@href').extract()
    		items.append(item)
        return items