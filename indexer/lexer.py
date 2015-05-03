from os import path
import re

from model.model import Page
from parser.html import HTMLParser

class StopWords:
    """ A collection of words which should be omitted from indexing """
    
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
        # A crappy hack in order to load all stop words because i'm lazy :)
        
        path_to_stop_words = path.realpath('docs/ressources/stop_words.txt')
        with open(path_to_stop_words) as file:
            stop_words = file.read()
        StopWords.words = eval('[' + stop_words  + ']')

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
            raise TypeError('The specified page must be an instance of Page');
        self.__page = page

    def tokens(self):
        """  
            Create iterator which can be used to iterate 
            over all tokens of the current page.
        """
        tokens = self.__get_tokens()
        for token in tokens:
            token = token.strip()
            token = token.lower()
            if self.__is_stopword(token):
                continue
            yield token

    def __get_tokens(self):
        content = self.__page.content
        tokens = re.split('[\s\.,!\-?:;]', content)
        return tokens

    def __is_stopword(self, token):
        return StopWords.is_stop_word(token)



def load_page():
    test_file = path.join(path.dirname(__file__), '../docs/ressources/d01.html')
    with open(test_file, 'r') as file:
        page = file.read()
    parser = HTMLParser()
    return parser.parse(page)
    

