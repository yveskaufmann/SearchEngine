from crawler.Crawler import Crawler
from indexer.indexer import Indexer
from analyzer.cosinus import CosinusAnalyzer
from utils.string import StringUtil

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
    link_structure_txt = pages.get_link_structure_text()
    print(link_structure_txt)

    # Print your index
    print(indexer.index)

    # Print the content of the pages
    print(pages)

    example_queries = ['tokens', 'index', 'tokens classification' ]
    analyzer = CosinusAnalyzer(indexer.index, crawler.pages)
    print(analyzer.get_length_of_pages_text())

    print(StringUtil.header('cosine_scores.txt'))
    for query in example_queries:
        hits = analyzer.analyze(query)
        print(hits)
    print()

    print(StringUtil.header('Cosinus combined with Page Rank'))
    analyzer = CosinusAnalyzer(indexer.index, crawler.pages, combine_with_page_rank=True)
    for query in example_queries:
        hits = analyzer.analyze(query)
        print(hits)
    print()

    row = 0
    matrix = []
    for page in pages:
        outlinks = []
        for c in range(1, pages.count() + 1):
            title = "d0" + str(c)
            outlinks.append(page.out_pages.has_page_with_title(title))
        matrix.append(outlinks)
        row += 1
    print(matrix)

