__author__ = 'Yves'

import unittest
from parser.html import HTMLParser
from os.path import join, dirname 

class TestHTMLParser(unittest.TestCase):
    
    def test_parseDummyPage_LinksShouldBeExtracted(self):
        parse_result = self.parse_page()
        expected_links = [ 'd{0:02}.html'.format(i)  for i in range(2, 5) ]
        self.assertListEqual(parse_result.out_links, expected_links) 

    def test_parseDummyPage_LeadingAndTraillingWhitespacesShouldRemovedFromContent(self):
        parse_result = self.parse_page()
        self.assertRegex(parse_result.content, '^[^\s]+.*[^\s]$')
    
    def test_parseDummyPage_ContentIsExtracted(self):
        expected_content = 'Python hates me :)'
        parse_result = self.parse_page('<html><body>' + expected_content + '</body></html>')
        self.assertEqual(expected_content, parse_result.content)
    
    def parse_page(self, page = None):
        parser = HTMLParser()
        page = parser.parse(self.get_dummy_page() if page is None else page)
        return page

    def get_dummy_page(self, page_id = 1):
        dummy_file_path = join(dirname(__file__), '../docs/ressources/d{0:02}.html'.format(page_id))
        with open(dummy_file_path) as dummy_file:
            return dummy_file.read()




if __name__ == '__main__':
    unittest.main()

