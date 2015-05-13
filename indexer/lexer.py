import re

from model.page import Page
from utils.path import RessourceUtil

class StopWords:
    """
    A collection of words which should be omitted from indexing.
    """

    def get():
        """
        Returns a list of stop words which are
        stored in the stop_words.txt.

        Notice: The stop_word.txt will be loaded
        only once if you need to reload the stop words
        please use StopWords.load().
        """

        if not hasattr(StopWords, 'words'):
            StopWords.load()

        return StopWords.words

    def is_stop_word(token):
        """
        Determines if a given token/string is a stop word
        and returns True in this case.
        """
        token = token.strip()
        if token == '':
            return True
        return token in StopWords.get()

    def load():
        """
        Load the stop words from
        the file docs/ressources/stop_words.txt.
        """

        stop_words = RessourceUtil.get_content_from_ressource('stop_words.txt')
        # A crappy hack in order to load all stop words because i'm lazy :)
        StopWords.words = eval('[' + stop_words + ']')

class TokenNormalizer:
    @staticmethod
    def normalize(token):
        token = token.strip()
        token = token.lower()
        return token

class TokenLexer:
    """
    Split a given page into a sequence of normalized tokens.
    and omit stop words.
    """

    def __init__(self, page):
        """
        Create a TokenLexer for a specific page.
        """

        if not isinstance(page, Page):
            raise TypeError('The specified page must be an instance of Page')
        self.__page = page

    def tokens(self):
        """
        Create iterator which can be used to iterate
        over all tokens of the current page.
        """

        tokens = self.__get_tokens()
        for token in tokens:
            token = TokenNormalizer.normalize(token)
            if self.__is_stopword(token):
                continue
            yield token

    def __get_tokens(self):
        content = self.__page.content
        tokens = re.split('[\s\.,!\-?:;]', content)
        return tokens

    def __is_stopword(self, token):
        return StopWords.is_stop_word(token)







