#   _________                           .__      ___________              .__
#  /   _____/ ____ _____ _______   ____ |  |__   \_   _____/ ____    ____ |__| ____   ____
#  \_____  \_/ __ \\__  \\_  __ \_/ ___\|  |  \   |    __)_ /    \  / ___\|  |/    \_/ __ \
#  /        \  ___/ / __ \|  | \/\  \___|   Y  \  |        \   |  \/ /_/  >  |   |  \  ___/
# /_______  /\___  >____  /__|    \___  >___|  / /_______  /___|  /\___  /|__|___|  /\___  >
#        \/     \/     \/            \/     \/          \/     \//_____/         \/     \/
#
# Version 1.0
#
# by Pascal, Hannah, Yves
#

from crawler.Crawler import Crawler
from indexer.indexer import Indexer
from analyzer.cosinus import CosinusAnalyzer
from utils.string import StringUtil
from pagerank.page_rank import Page_Rank

def main():
    """ An example how the search engine could be used.  """

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

    # Print the content of the pages
    print(pages)

    # Print the link structure
    link_structure_txt = pages.get_link_structure_text()
    print(link_structure_txt)

    # Printing and creation of the index
    indexer = Indexer()
    indexer.index_pages(pages)
    index = indexer.index
    print(index)

    # Calculation and Printing of Page Rank
    pagerank = Page_Rank()
    pagerank.fill_matrix(crawler)
    pagerank.calculate_probabilities(0.05, 0.95)
    pagerank.calculate_page_rank(0.04)
    print()

    # Scoring
    example_queries = ['tokens', 'index', 'classification', 'tokens classification' ]
    analyzer = CosinusAnalyzer(index, pages)
    print(analyzer.get_length_of_pages_text())

    # Cosinus Scoring
    print(StringUtil.header('cosine_scores.txt'))
    for query in example_queries:
        hits = analyzer.analyze(query)
        print(hits)
    print()

    # Cosinus Scoring combined with the page rank.
    print(StringUtil.header('Cosinus combined with Page Rank'))
    for query in example_queries:
        hits = analyzer.analyze(query, combine_with_page_rank=True)
        print(hits)
    print()

if __name__ == '__main__':
    main()



