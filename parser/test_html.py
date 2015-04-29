import unittest
from parser.html import HTMLParser

class TestHTMLParser(unittest.TestCase):
    
    def test_parseDummyPage_ContentIsExtracted(self):
        parser = HTMLParser()
        dummy_page = self.get_dummy_page()
        
        parser.parse(dummy_page)

        expected_links = [ 'd{0:02}.html'.format(i)  for i in range(2, 5) ]
        self.assertListEqual(parser.get_out_links(), expected_links) 

    def get_dummy_page(self):
        with open('dummy.html') as dummy_file:
            return dummy_file.read()


if __name__ == '__main__':
    unittest.main()