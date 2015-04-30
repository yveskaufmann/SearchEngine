__author__ = 'Yves'

import unittest
import os
from model.model import Index

class TestIndex(unittest.TestCase):
    
    def test_createDummyIndex_str_outputIsAsExpected(self):
        dummyIndex = Index()

        dummyIndex.add_Token_from_docment('DaDaDa', 1)
        dummyIndex.add_Token_from_docment('DaDaDa', 1)
        dummyIndex.add_Token_from_docment('DumDiDum', 2)
        dummyIndex.add_Token_from_docment('DumDiDum', 3)
        
        expected_output = os.linesep.join([
            "(DaDaDa, df:1) -> [('1', 2)]", 
            "(DumDiDum, df:2) -> [('2', 1), ('3', 1)]"
        ])

        self.assertEqual(expected_output, str(dummyIndex))




if __name__ == '__main__':
    unittest.main()

