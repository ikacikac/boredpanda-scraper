# -*- coding: utf-8 -*-

# Scrapy settings for boredpanda_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os

SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
SCRAPER_DIR = os.path.join(SETTINGS_DIR, '..')

BOT_NAME = 'boredpanda_scraper'

SPIDER_MODULES = ['boredpanda_scraper.spiders']
NEWSPIDER_MODULE = 'boredpanda_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'boredpanda_scraper (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'boredpanda_scraper.pipelines.BoredpandaImagePipeline': 1,
    'boredpanda_scraper.pipelines.BoredpandaSQLitePipeline': 2
}

IMAGES_STORE = os.path.join(SCRAPER_DIR, 'images')

IMAGES_THUMBS = {
    'big': (270, 270),
}

# Enabling CSV exporter
FEED_EXPORTERS = {
    'csv': 'boredpanda_scraper.exporters.csvexporter.CSVExporter'
}

# Specifying order of fields exported in CSV file.
EXPORT_FIELDS = ['title', 'content', 'votes',
                 'date_created', 'images',
                 'image_urls', 'url']

DOWNLOAD_DELAY = 2

DB_PATH = os.path.join(SCRAPER_DIR, 'test.db')