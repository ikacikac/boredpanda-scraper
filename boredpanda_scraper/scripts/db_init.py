#!/usr/bin/env python2.7

import sqlite3
import os

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
SCRAPER_DIR = os.path.join(SCRIPT_DIR, '../..')
DB_PATH = os.path.join(SCRAPER_DIR, 'test.db')

conn = sqlite3.connect(DB_PATH)

cur = conn.cursor()


query = '''

CREATE TABLE articles (
  id INTEGER PRIMARY KEY,
  title TEXT UNIQUE,
  content TEXT,
  votes INTEGER,
  date_created TEXT
);

CREATE TABLE images (
  id INTEGER PRIMARY KEY,
  path TEXT,
  url TEXT,
  article_id INTEGER,
  date_created TEXT,
  FOREIGN KEY(article_id) REFERENCES articles(id)
);

'''

try:
    res = cur.executescript(query)
except sqlite3.OperationalError:
    raise Exception('There was an error executing query.')


cur.close()
conn.close()