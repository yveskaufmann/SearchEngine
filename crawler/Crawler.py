import os
import re

from parser.html import HTMLParser
from utils.path import RessourceUtil

__author__ = 'pascal'

class Crawler:

    data = []

    @staticmethod
    def string_for_url(url):
        with open(url, "r") as file:
            return file.read()

    @DeprecationWarning #Please use util.path.RessourceUtil.get_ressource_path instead of get_path_for_material
    @staticmethod
    def get_path_for_material(file_name):
        material_dir = os.path.join(os.path.dirname(__file__), os.pardir, "docs", "ressources")
        return os.path.join(material_dir, file_name)

    @staticmethod
    def print_page(page):
        """handy method for printing Page objects"""
        print("\n\n" + page.title + " \n===")
        print("url: \n¯¯¯¯\n" + page.url)
        print("content: \n¯¯¯¯¯¯¯¯\n" + page.content)
        print("out_links: \n¯¯¯¯¯¯¯¯¯¯")
        for link in page.out_links:
            print(link)

    @DeprecationWarning #Please check if you need this method, because HTMLParser ignores empty lines by default.
    @staticmethod
    def remove_empty_lines(txt):
        new_txt = ""
        for line in txt.splitlines():
            regex = re.compile(r"^[^\s][^\n][a-zA-Z0-9]*.*$")
            if regex.match(line):
                new_txt += line + "\n"
        return new_txt

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

    def already_fetched_url(self, url):
        for page in self.data:
            if page.url == url:
                return True
        return False

    def get_link_structure_text(self):
        """Prints an array of pages, just like in link_structure.txt"""
        sorted_pages = sorted(self.data, key=lambda p: p.title)
        result = ""
        for page in sorted_pages:
            outlink_titles = ""
            count = 0
            for url in page.out_links:
                count += 1
                link = self.page_for_url(url)
                outlink_titles += link.title
                if count != len(page.out_links):
                    outlink_titles += ","
            result += page.title + ":" + outlink_titles + "\n"
        return result

    def put_url_in_cache(self, url):
        if url not in self.url_cache:
            self.url_cache.append(url)

    def page_for_url(self, url):
        for page in self.data:
            if page.url == url:
                return page

    def page_for_title(self, title):
        for page in self.data:
            if page.title == title:
                return page

    def extract_data_and_get_out_links(self, url):
        txt = Crawler.string_for_url(url)
        
        parser = HTMLParser()
        page = parser.parse(txt, base_url=RessourceUtil.get_ressource_path())
        page.url = url

        self.data.append(page)
        return page.out_links

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
