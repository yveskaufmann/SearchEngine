import unittest

from indexer.lexer import StopWords
from indexer.lexer import TokenLexer
from model.page import Page

class TestStopWords(unittest.TestCase):
    all_stop_words = [
        'd01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd07', 'd08', 'a',
        'also', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do',
        'for', 'have', 'is', 'in', 'it', 'of', 'or', 'see', 'so',
        'that', 'the', 'this', 'to', 'we'
    ]

    def test_get_AllStopWordsAreReturned(self):
        self.assertListEqual(TestStopWords.all_stop_words, StopWords.get())

    def test_is_stop_word_StopWordsAreDetected(self):

        all_stop_words = TestStopWords.all_stop_words
        all_words_are_stop_words = all(map(StopWords.is_stop_word, all_stop_words))

        self.assertTrue(all_words_are_stop_words, msg='Not all stop words are detected')
        self.assertFalse(StopWords.is_stop_word('token'), msg='Token is no stop word')

class TestTokenLexer(unittest.TestCase):
    def test_tokens_AllExpectedTokensAreReturned(self):
        page = Page()
        page.content = "yEaH,PYthON?!,. is   not  . so,!? bad, as i thought:."

        lexer = TokenLexer(page)
        tokens = list(lexer.tokens())

        self.assertListEqual(tokens, [
            'yeah', 'python', 'not',
            'bad', 'i', 'thought'
        ])


if __name__ == '__main__':
    unittest.main()
