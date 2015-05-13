import math

from model.index import Index
from model.page import Pages
from model.page import Page
from indexer.lexer import TokenLexer

class CosinunsAnalyzer:

    def __init__(self, index, pages):

        if not isinstance(index, Index):
            raise TypeError('index must be an instance of Index')

        if not isinstance(index, Pages):
            raise TypeError('index must be an instance of Index')

        self.index = index
        self.pages = pages
        self.N = pages.count()

    def analyze(self, query):
        """ Analyze a given query and returns the corresponding hits """

        for term in self.query_to_tokens(query):
            wtq = 1  # TODO how ?
            posting_list = self.index.get_posting_list(term)

            for doc_id, doc_meta in posting_list.items():
                term_frequency = doc_meta.term_frequency
                # TF-idf weight
                wtd = self.log_weight_frequency(term_frequency) * self.idf_for_term(term)
                score = wtd * wtq


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


