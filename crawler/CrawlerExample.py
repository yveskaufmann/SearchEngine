__author__ = 'pascal'

from crawler.Crawler import Crawler
from indexer.indexer import Indexer
from utils.path import RessourceUtil

#  _____                           _
# | ____|_  ____ _ _ __ ___  _ __ | | ___
# |  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \
# | |___ >  < (_| | | | | | | |_) | |  __/
# |_____/_/\_\__,_|_| |_| |_| .__/|_|\___|
#                           |_|

def crawler_example():

    # Create a seed
    seed = [
        RessourceUtil.get_ressource_path('d01.html'),
        RessourceUtil.get_ressource_path('d06.html'),
        RessourceUtil.get_ressource_path('d08.html')
    ]
    
    # Instatiate the crawler.
    crawler = Crawler()

    # Start the crawler with the seed.
    crawler.start_crawling(seed)

    # Access the data.
    crawler.data

    # Print the data...
    for page in crawler.data:
    # # ... with print_page(page_object)
        Crawler.print_page(page)

    # Print the link structure
    link_structure_txt = crawler.get_link_structure_text()
    print(link_structure_txt)

    # Create an Indexer 
    indexer = Indexer()

    # Index the pages
    indexer.index_pages(*crawler.data)

    # Print your index 
    print(indexer.index)

    



