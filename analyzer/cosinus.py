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

    def caclulate_length(self):
        docs = {}
        for term, meta in self.index.items():
            for doc_id, doc in meta['postings'].items():
                if doc_id not in docs:
                    docs[doc_id] = []
                if meta['document_frequency'] > 0:
                    tfidf = (1 + math.log10(doc['term_frequency'])) * math.log10(float(self.N / meta['document_frequency'] ))
                    docs[doc_id].append(tfidf)

        for doc_id, doc in docs.items():
            docs[doc_id] = math.sqrt(sum([x**2 for x in doc]))

        return docs

    def analyze(self, query):
        """ Analyze a given query and returns the corresponding hits """

        query_terms = [ query for query in self.query_to_tokens(query) ]

        # Vector length calculation
        length = self.caclulate_length()
        query_length = 0
        for term in query_terms:
            query_length += self.idf_weight(term) ** 2
        query_length = math.sqrt(query_length)
        hits = {}

        # Score terms
        for term in query_terms:
            wtq = self.idf_weight(term)
            posting_list = self.index.get_posting_list(term)
            for doc_id, doc_meta in posting_list.items():
                if doc_id not in hits:
                    hits[doc_id] = {'score': 0, 'length': 0}

                term_frequency = doc_meta['term_frequency']
                tf_weight = self.log_weight_frequency(term_frequency)
                idf_weight = self.idf_weight(term)
                tf_idf_weight = tf_weight * idf_weight

                hits[doc_id]['score'] += tf_idf_weight * wtq

        # Normalize score vectors
        for doc_id, hit in hits.items():
            hit['score'] = hit['score'] / length[doc_id]
            hit['score'] = hit['score'] / query_length

        for doc_id, hit in sorted(hits.items(), key=lambda h: h[1]['score'], reverse=True):
            yield doc_id + ": " + str(hit['score'])

    def log_weight_frequency(self, frequence):
        """ Calculate the log frequency weight """
        if frequence >= 0:
            return 1 + math.log10(frequence)
        return 0

    def idf_weight(self, term):
        if term not in self.index:
            return 0
        dft = self.index.get_document_frequency(term)
        return math.log10(float(self.N / dft))

    def query_to_tokens(self, query):
        page = Page()
        page.content = query
        lexer = TokenLexer(page)
        return lexer.tokens()


