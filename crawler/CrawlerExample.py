from crawler.Crawler import Crawler
from indexer.indexer import Indexer
from analyzer.cosinus import CosinunsAnalyzer

__author__ = 'pascal'

#  _____                           _
# | ____|_  ____ _ _ __ ___  _ __ | | ___
# |  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \
# | |___ >  < (_| | | | | | | |_) | |  __/
# |_____/_/\_\__,_|_| |_| |_| .__/|_|\___|
#                           |_|

def crawler_example():
    # Create a seed
    seed = [
        'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html',
        'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html',
        'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html'
    ]

    # Instatiate the crawler.
    crawler = Crawler()

    # Start the crawler with the seed.
    crawler.start_crawling(seed)

    # Access the pages.
    pages = crawler.pages

    # Create an Indexer
    indexer = Indexer()

    # Index the pages
    indexer.index_pages(pages)

    # Print the link structure
    link_structure_txt = crawler.get_link_structure_text()
    print(link_structure_txt)

    # Print your index
    print(indexer.index)

    # Print the content of the pages
    print(pages)

    analyzer = CosinunsAnalyzer(indexer.index, crawler.pages)
    ret = analyzer.analyze("tokens classification")
    print(list(ret))
