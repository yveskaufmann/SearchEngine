import math

from model.index import Index
from model.page import Pages
from model.page import Page
from indexer.lexer import TokenLexer

class CosinunsAnalyzer:

    def __init__(self, index, pages):

        if not isinstance(index, Index):
            raise TypeError('index must be an instance of Index')

        if not isinstance(pages, Pages):
            raise TypeError('index must be an instance of Index')

        self.index = index
        self.pages = pages
        self.N = pages.count()

    def prepare_index(self):
        for term, meta in self.index.items():
            pass

    def analyze(self, query):
        """ Analyze a given query and returns the corresponding hits """

        self.prepare_index()
        hits = {}
        for term in self.query_to_tokens(query):
            wtq = self.idf_for_term(term)  # log(N / dtf)
            posting_list = self.index.get_posting_list(term)
            for doc_id, doc_meta in posting_list.items():
                if doc_id not in hits:
                    hits[doc_id] = {'score': 0, 'length': 0}
                term_frequency = doc_meta['term_frequency']
                # TF-idf weight
                wtd = self.log_weight_frequency(term_frequency) * self.idf_for_term(term)
                score = wtd * wtq
                hits[doc_id]['score'] += score
                hits[doc_id]['length'] += score * score

        for doc_id, hit in hits.items():
            hit['score'] = hit['score']

        for doc_id, hit in sorted(hits.items(), key=lambda h: h[1]['score'], reverse=True):
            yield doc_id + ": " + str(hit['score'])

    def log_weight_frequency(self, frequence):
        """ Calculate the log frequency weight """
        if frequence >= 0:
            return 1 + math.log10(frequence)
        return 0

    def idf_for_term(self, term):
        if term not in self.index:
            return 0
        dft = self.index.get_document_frequency(term)
        return math.log10(self.N / math.log10(dft))

    def query_to_tokens(self, query):
        page = Page()
        page.content = query
        lexer = TokenLexer(page)
        return lexer.tokens()


