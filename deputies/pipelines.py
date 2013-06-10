# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
#from slugify import slugify


class DeputiesPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):

    def __init__(self, item):
        super(ImagesPipeline, self).__init__()

    #def image_key(self, item, url):
    #    id_dep = item['id_dep']
    #    nome = slugify(item['nome'])
    #    return 'full/%s-%s.jpg' % (id_dep, nome)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def image_key(self, url):
        image_guid = url.split('/')[-1]
        return 'full/%s' % (image_guid)
