import unittest
import os

from model.model import Index
from model.model import Page

class TestPage(unittest.TestCase):
    
    def test_str_outputStringIsAsExpected(self):
        test_page = Page()
        test_page.title = 'D01'
        test_page.content = 'Bla Bla Blub'

        expected_output = os.linesep.join([
            '---------------------------------------------------------------------------',
            'D01',
            '---------------------------------------------------------------------------',
            'Bla Bla Blub'
        ])
        
        self.assertEqual(expected_output, str(test_page))


class TestIndex(unittest.TestCase):
    
    def test_createDummyIndex_str_outputStringIsAsExpected(self):
        dummyIndex = Index()

        dummyIndex.register_Token('DaDaDa', 1)
        dummyIndex.register_Token('DaDaDa', 1)
        dummyIndex.register_Token('DumDiDum', 2)
        dummyIndex.register_Token('DumDiDum', 3)
        
        expected_output = os.linesep.join([
            'index.txt',
            '¯¯¯¯¯¯¯¯¯',
            '(DaDaDa, df:1) -> [(\'1\', 2)]', 
            '(DumDiDum, df:2) -> [(\'2\', 1), (\'3\', 1)]'
        ])

        self.assertEqual(expected_output, str(dummyIndex))
        
if __name__ == '__main__':
    unittest.main()
