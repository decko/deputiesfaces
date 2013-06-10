# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DeputiesItem(Item):
    id_dep = Field()
    nome = Field()
    url = Field()
    email = Field()
    image_urls = Field()
    images = Field()
