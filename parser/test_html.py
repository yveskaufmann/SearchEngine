import re
import unittest

from parser.html import HTMLParser
from utils.path import RessourceUtil

__author__ = 'Yves'

class TestHTMLParser(unittest.TestCase):
    
    def test_parseDummyPage_LinksShouldBeExtracted(self):
        parse_result = self.parse_page()
        expected_links = ['d{0:02}.html'.format(i) for i in range(2, 5)]
        self.assertListEqual(parse_result.out_links, expected_links) 

    def test_parseDummyPage_LeadingAndTraillingSpacesShouldRemovedFromContent(self):
        parse_result = self.parse_page()
        pattern_leading_and_trailing_spaces = re.compile('^[^\s]+.*[^\s]$', re.M)
        self.assertRegex(parse_result.content, pattern_leading_and_trailing_spaces)
    
    def test_parseDummyPage_ContentIsExtracted(self): 
        expected_content = 'Python hates me :)'
        parse_result = self.parse_page('<html><body>' + expected_content + '</body></html>')
        self.assertEqual(expected_content, parse_result.content)

    def test_parseDummyPageWithBaseURL_ExtractedLinksAreAbsolut(self):
        parse_result = self.parse_page(base_url='http://host/path/')
        expected_links = [
            'http://host/path/d02.html',
            'http://host/path/d03.html',
            'http://host/path/d04.html'
        ]

        self.assertListEqual(expected_links, parse_result.out_links)
    
    def parse_page(self, pageid_or_content=1, base_url='.'):
        
        content = pageid_or_content
        if isinstance(pageid_or_content, int):
            ressource = 'd{0:02}.html'.format(pageid_or_content)
            content = RessourceUtil.get_content_from_ressource(ressource)
        
        parser = HTMLParser()
        return parser.parse(content, base_url=base_url)

if __name__ == '__main__': 
    unittest.main()
