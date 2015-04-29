__author__ = 'pascal'

from bs4 import BeautifulSoup
from model.model import Page
import os

def get_path_for_material(file_name):
    material_dir = os.path.join(os.getcwd(), os.pardir, "unterlagen/material")
    return os.path.join(material_dir, file_name)

def print_page(page):
    print("\n\n" + page.title + " \n===")
    print("url: " + page.url)
    print("content: " + page.content)
    print("out_links: ")
    for link in page.out_links:
        print(link)

class Crawler:

    data = []

    def string_for_url(self, url):
        with open(url, "r") as file:
            return file.read()

    def already_fetched_url(self, url):
        for page in self.data:
            if page.url == url:
                return True
        return False

    def put_url_in_cache(self, url):
        if url not in self.url_cache:
                self.url_cache.append(url)

    def extract_data_and_get_out_links(self, url):
        txt = self.string_for_url(url)
        soup = BeautifulSoup(txt)
        page = Page()
        page.url = url
        page.title = soup.title.string
        out_links = []
        for out_link in soup.findAll("a"):
            out_links.append(get_path_for_material(out_link["href"]))
        page.out_links = out_links
        self.data.append(page)
        return out_links

    def merge_without_duplicates(self, target_list, source_list):
        unseen_list = []
        for url in source_list:
            if url not in target_list:
                target_list.append(url)
                unseen_list.append(url)
        return unseen_list

    def calculate_difference(self, target_list, source_list):
        difference = []
        for url in source_list:
            if url not in target_list:
                difference.append(url)
        return difference

    def start_crawling(self, seed):
        self.url_cache = list(seed)
        url_db = list(seed)
        while self.url_cache != []:
            unseen_links = []
            while True:
                url = self.url_cache.pop(0)
                # OUTLINKS
                out_links = (self.extract_data_and_get_out_links(url))
                tmp_links = self.merge_without_duplicates(url_db, out_links)
                self.merge_without_duplicates(unseen_links, tmp_links)
                if not self.url_cache:
                    self.url_cache = unseen_links
                    break
        for page in self.data:
            print_page(page)


d01 = get_path_for_material("d01.html")
d02 = get_path_for_material("d02.html")
d03 = get_path_for_material("d03.html")
d04 = get_path_for_material("d04.html")
d05 = get_path_for_material("d05.html")
d06 = get_path_for_material("d06.html")
d07 = get_path_for_material("d07.html")
d08 = get_path_for_material("d08.html")

crawler = Crawler()
crawler.start_crawling([d01, d06, d08])