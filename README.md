# boredpanda-scraper
This project is an example Scrapy project with basics on how it should be implemented. 
It should be used solely for educational purposes.


##How to

To initialize project and generate crawling spider on Linux operating system you will need Python 2.7, Scrapy 0.24 (used for this project), and some Bash shell working knowledge.

Next sequence of commands was used to initialize project and generate crawling spider that will be used to crawl Bored Panda.

```
* scrapy startproject boredpanda_scraper
* cd boredpanda_scraper
* scrapy genspider --template=crawl boredpanda boredpanda.com
```

After this, you can implement your own crawling bot or you can clone this repository and run example by running:

```
scrapy crawl boredpanda
```

in Linux console while positioned in boredpanda_scraper folder.

Have fun learning!
