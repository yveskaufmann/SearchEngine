import math
import os

from analyzer.hit import Hit
from analyzer.hit import Hits
from model.index import Index
from model.page import Page
from model.page import Pages
from indexer.lexer import TokenLexer
from utils.string import StringUtil

class CosinusAnalyzer:

    def __init__(self, index, pages, combine_with_page_rank=False):

        if not isinstance(index, Index):
            raise TypeError('index must be an instance of Index')

        if not isinstance(pages, Pages):
            raise TypeError('index must be an instance of Index')

        self.index = index
        self.count_of_pages = pages.count()
        self.pages = pages
        self.length_of_pages = self.caclulate_length_of_pages()
        self.combine_with_page_rank = combine_with_page_rank

    def analyze(self, query):
        """
        Analyze a given query and returns the corresponding hits
        """

        query_length = 0
        page_scores = {}
        query_tokens = self.__query_to_tokens(query)

        # Calculate page_scores
        for term in query_tokens:
            wtq = self.idf_weight(term)
            query_length += wtq ** 2
            for page_id in self.index.get_posting_list(term):
                tf_idf_weight = self.tf_idf_weight(term, page_id)
                if page_id not in page_scores:
                    page_scores[page_id] = 0
                page_scores[page_id] += tf_idf_weight * wtq

        query_length = math.sqrt(query_length)

        # Normalize score vectors and build the hit list
        hits = Hits(query_tokens)
        for page_id, score in page_scores.items():
            hit = Hit(page_id, score)
            hit.score /= self.length_of_pages[page_id]
            hit.score /= query_length

            if ( self.combine_with_page_rank ):
                hit.score *= self.pages.get_page_by_title(page_id).page_rank

            hits.append(hit)

        hits.sort()

        return hits

    def caclulate_length_of_pages(self):
        """
        Calculate the length of the vector space for each page in the index
        """
        page_lengths = {}
        for term in self.index:
            for page_id in self.index.get_posting_list(term):
                if page_id not in page_lengths:
                    page_lengths[page_id] = 0

                tf_idf_weight = self.tf_idf_weight(term, page_id)
                page_lengths[page_id] += tf_idf_weight ** 2

        for page_id, page in page_lengths.items():
            page_lengths[page_id] = math.sqrt(page_lengths[page_id])

        return page_lengths

    def get_length_of_pages_text(self):
        """
        Create the string representation for the length of pages
        vector.
        """
        output = [StringUtil.header('doc_lengthes.txt')]
        for page_id in sorted(self.length_of_pages):
            length_entry = page_id + ':' + ' ' * 4 + str(self.length_of_pages[page_id])
            output.append(length_entry)

        return os.linesep.join(output) + os.linesep

    def tf_idf_weight(self, term, page_id):
        """
        Calculate the tf-idf weight for the term in the page
        with the id 'page_id'.
        """
        return self.tf_weight(term, page_id) * self.idf_weight(term)

    def tf_weight(self, term, page_id):
        """
        Calculate log frequency weight of the term in the page
        with the id 'page_id'.
        """
        frequence = self.index.get_term_frequency(term, page_id)
        if frequence > 0:
            return 1 + math.log10(frequence)
        return 0

    def idf_weight(self, term):
        """
        Calculate idf weight of the term,
        idf is a measure of the informativeness of the term.
        """
        if term not in self.index:
            return 0
        dft = self.index.get_document_frequency(term)
        return math.log10(float(self.count_of_pages / dft))

    def __query_to_tokens(self, query):
        """
        Split the query into tokens
        """
        page = Page()
        page.content = query
        lexer = TokenLexer(page)
        return list(lexer.tokens())


