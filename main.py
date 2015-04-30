from crawler.Crawler import Crawler
from crawler.CrawlerExample import crawler_example

seed = [
    Crawler.get_path_for_material("d01.html"),
    Crawler.get_path_for_material("d06.html"),
    Crawler.get_path_for_material("d08.html")
]

crawler = Crawler()
crawler.start_crawling(seed)

# check it out
crawler_example()



