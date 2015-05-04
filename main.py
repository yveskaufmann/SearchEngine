from crawler.Crawler import Crawler
from crawler.CrawlerExample import crawler_example
from utils.path import RessourceUtil

seed = [
    RessourceUtil.get_ressource_path('d01.html'),
    RessourceUtil.get_ressource_path('d06.html'),
    RessourceUtil.get_ressource_path('d08.html')
]

crawler = Crawler()
crawler.start_crawling(seed)

# check it out
crawler_example() 



