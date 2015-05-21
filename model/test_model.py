import unittest
import os

from model.index import Index
from model.page import Page

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
        expected_output = os.linesep.join([
            'index.txt',
            '¯¯¯¯¯¯¯¯¯',
            '(DaDaDa, df:1) -> [(\'d01\', 2)]',
            '(DumDiDum, df:2) -> [(\'d02\', 1), (\'d03\', 1)]',
            ''
        ])

        self.assertEqual(expected_output, str(self.get_dummy_index()))

    def test_get_posting_list_postingListIsComplete(self):
        index = self.get_dummy_index()

        posting_list = index.get_posting_list('daDadA')
        self.assertListEqual(posting_list, ['d01'])

        posting_list = index.get_posting_list('DaDaDa', 'dumDIDum')
        self.assertListEqua(posting_list, ['d{0:02}'.format(n) for n in range(1, 4)])

    def get_dummy_index(self):
        dummyIndex = Index()
        dummyIndex.register_Token('DaDaDa', 'd01')
        dummyIndex.register_Token('DaDaDa', 'd01')
        dummyIndex.register_Token('DumDiDum', 'd02')
        dummyIndex.register_Token('DumDiDum', 'd03')

        return dummyIndex


if __name__ == '__main__':
    unittest.main()
