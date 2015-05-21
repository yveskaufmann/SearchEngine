from urllib.request import urlopen

from model.page import Pages
from parser.html import HTMLParser

__author__ = 'pascal'

class Crawler:

    def __init__(self):
        self.pages = Pages()

    @staticmethod
    def merge_without_duplicates(target_list, source_list):
        """Merges source_list into target_list without creating duplicates.
        Returns all elements, that weren't in target_list before"""
        unseen_list = []
        for url in source_list:
            if url not in target_list:
                target_list.append(url)
                unseen_list.append(url)
        return unseen_list

    @staticmethod
    def calculate_difference(target_list, source_list):
        """Returns all elements from sour_list, that aren't in target_list."""
        difference = []
        for url in source_list:
            if url not in target_list:
                difference.append(url)
        return difference

    def extract_data_and_get_out_links(self, url):
        txt = urlopen(url).read()
        parser = HTMLParser()
        page = parser.parse(txt, url)
        self.pages.append(page)
        return page.out_links

    def fill_pages_with_outpages(self):
        for page in self.pages:
            for out_link in page.out_links:
                outpage = self.pages.get_page_by_url(out_link)
                if outpage is not None:
                    page.out_pages.append(outpage)

    def start_crawling(self, seed):
        self.url_cache = list(seed)
        url_db = list(seed)

        while self.url_cache != []:
            unseen_links = []
            while True:
                url = self.url_cache.pop(0)
                out_links = (self.extract_data_and_get_out_links(url))
                tmp_links = self.merge_without_duplicates(url_db, out_links)
                self.merge_without_duplicates(unseen_links, tmp_links)
                if not self.url_cache:
                    self.url_cache = unseen_links
                    break

        self.pages.sort()
        self.fill_pages_with_outpages()
