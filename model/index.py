import os
import copy

from utils.string import StringUtil

class Index:

    def __init__(self):
        self.__terms = {}

    def register_Token(self, token, document_title):
        """
        Register a Token which was found in a specific document.
        """

        term = self.__get_term_if_exists_or_create_one(token)
        if document_title not in term['postings']:
            term['postings'][document_title] = {'term_frequency': 0}
            term['document_frequency'] += 1

        term['postings'][document_title]['term_frequency'] += 1

    def get_posting_list(self, token):
        """
        Returns the posting list for a given term if
        it is in the index otherwise None will be returned.
        """

        term = self.__normalize(token)
        if term in self.__terms:
            return copy.deepcopy(self.__terms[term]['postings'])

        return None

    def get_document_frequency(self, token):
        """
        Returns the document frequency (df_t), the
        number of documents that term occurs in.
        """
        term = self.__normalize(token)
        if term in self.__terms:
            return self.__terms[term]['document_frequency']

        return 0

    def __contains__(self, token):
        term = self.normalize(token)
        return term in self.__terms

    def __str__(self):
        """
        Create the required string representation of an
        index for more details see docs/results/index.txt

        For example a possible output could be:

        index.txt
        ¯¯¯¯¯¯¯¯¯
        (advance, df:1) -> [('d04', 1)]
        (algorithm, df:1) -> [('d07', 1)]
        (documents, df:3) -> [('d04', 1), ('d07', 1), ('d05', 1)]
        ...
        """

        header = StringUtil.header('index.txt')

        output = []
        output.append(header)
        output.append('')

        for token, term in sorted(self.__terms.items()):

            list_of_postings = [self.__render_postings(id, doc) for id, doc in sorted(term['postings'].items())]
            list_of_postings = ', '.join(list_of_postings)

            newLine = "({0}, df:{1}) -> [{2}]".format(token, term['document_frequency'], list_of_postings)
            output.append(newLine)

        return os.linesep.join(output) + os.linesep

    def __render_postings(self, id, doc):
        return "('{0}', {1})".format(id, doc['term_frequency'])

    def __get_term_if_exists_or_create_one(self, token):
        """
        Return registered token or create a new one
        if the specified token isn't already registered
        """

        if token in self.__terms:
            return self.__terms[token]

        self.__terms[token] = {
            'postings': dict(),
            'document_frequency': 0
        }

        return self.__terms[token]

    def __normalize(self, term):
        from indexer.lexer import TokenNormalizer
        return TokenNormalizer.normalize(term)
