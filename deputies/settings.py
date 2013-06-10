import os
CURRENT_DIR = os.path.dirname(__file__)

# Scrapy settings for deputies project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'deputies'

SPIDER_MODULES = ['deputies.spiders']
NEWSPIDER_MODULE = 'deputies.spiders'

ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
#ITEM_PIPELINES = ['deputies.pipelines.MyImagesPipeline']
IMAGES_STORE = os.path.join(CURRENT_DIR, 'images')

# Crawl responsibly by identifying yourself (and your website)
# on the user-agent
#USER_AGENT = 'deputies (+http://www.yourdomain.com)'
