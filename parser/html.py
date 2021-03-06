from bs4 import BeautifulSoup

from model.page import Page
from utils.list import ListUtil
from utils.url import URLUtils
import re

class HTMLParser:
    """
    Parser which extract out links and the
    text from a a given HTML content.
    """

    def parse(self, text, url):
        dom = self.parseDocument(text)
        page = Page()
        page.title = self.get_text_from_element('title')
        page.content = self.remove_a_tags(self.get_text_from_element('body'))
        page.url = url

        def read_link(link):
            return URLUtils.join_relurl_to_absurl(url, link['href'])

        page.out_links = [read_link(link) for link in dom.select('a[href]')]
        page.out_links = ListUtil.to_list_without_duplicated_entries(page.out_links)

        return page

    def remove_a_tags(self, txt):
        result = ''
        for line in txt.splitlines():
            match = re.sub(r'^(See also).*$', ' ', line)
            if match != '' and match != ' ':
                result += match + '\n'

        return result

    def parseDocument(self, text):
        self.dom = BeautifulSoup(text, 'html')
        return self.dom

    def get_text_from_element(self, query, default_value=''):
        found_element = self.dom.find(query)

        if found_element is None:
            return default_value

        return found_element.get_text(strip=False).strip()
