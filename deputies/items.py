# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DeputiesItem(Item):
    nome = Field()
    img = Field()
    url = Field()
    email = Field()
