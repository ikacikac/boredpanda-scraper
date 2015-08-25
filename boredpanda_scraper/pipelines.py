# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import sqlite3
from os import path


class BoredpandaImagePipeline(ImagesPipeline):

    def item_completed(self, results, item, info):
        file_paths = [(x['url'], x['path']) for ok, x in results if ok]
        if not file_paths:
            raise DropItem('No files downloaded '
                           'for item {}'.format(item['url']))
        item['images'] = file_paths
        return item


class BoredpandaSQLitePipeline(object):

    def __init__(self, path):
        self.db_path = path
        self.conn = None
        self.cur = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(path=crawler.settings.get('DB_PATH'))

    def open_spider(self, spider):
        if not path.isfile(self.db_path):
            raise Exception('Could not connect to database'
                            ' at {}'.format(self.db_path))
        else:
            self.conn = sqlite3.connect(self.db_path)
            self.cur = self.conn.cursor()

    def close_spider(self, spider):
        if not path.isfile(self.db_path):
            raise Exception('Could not close database connection.')
        else:
            self.cur.close()
            self.conn.close()

    def process_item(self, item, spider):
        cur = self.cur
        conn = self.conn

        # Article title is unique and querying article
        # by title will show if we already scraped it.
        query = 'SELECT * FROM articles WHERE title=?'
        cur.execute(query, (item.get('title'),))
        article_id = cur.fetchone()
        if article_id:
            raise DropItem('Item already in database.')

        # This is where new article gets inserted into db
        # and we keep article_id for inserting images.
        query = 'INSERT INTO articles ' \
                '(title, content, votes, date_created) ' \
                'VALUES (?, ?, ?, ?)'
        cur.execute(query, (item.get('title'),
                            item.get('content'),
                            item.get('votes'),
                            item.get('date_created')))
        article_id = cur.lastrowid

        query = 'INSERT INTO images ' \
                '(path, url, article_id, date_created) ' \
                'VALUES (?, ?, ?, ?)'
        cur.executemany(query, [(file_paths[1],
                                 file_paths[0],
                                 article_id,
                                 item.get('date_created'))
                                for file_paths in item['images']])

        conn.commit()
        return item