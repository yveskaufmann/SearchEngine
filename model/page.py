import os
from collections import UserList
from utils.string import StringUtil

class Page:

    def __init__(self):
        self.title = ""
        self.content = ""
        self.url = ""
        self.out_links = []

    def __str__(self):
        """
        Create the required string representation of a
        page. For a example of a possible output please
        see docs/results/docs.txt.
        """

        headline = StringUtil.line(75)
        page_str = os.linesep.join([
            headline,
            self.title,
            headline,
            self.content
        ])

        return page_str

    def print_debug_info(self):
        """ Handy method for printing debug informations for this page """
        print("\n\n" + self.title + " \n===")
        print("url: \n¯¯¯¯\n" + self.url)
        print("content: \n¯¯¯¯¯¯¯¯\n" + self.content)
        print("out_links: \n¯¯¯¯¯¯¯¯¯¯")
        for link in self.out_links:
            print(link)


class Pages(UserList):

    def __init__(self):
        super().__init__()

    def count(self):
        return len(self)

    def has_page_with_title(self, title):
        return self.get_page_by_title(title) is not None

    def has_page_with_url(self, url):
        return self.get_page_by_url(url) is not None

    def get_page_by_title(self, title):
        return self.filter(lambda page: page.title == title)

    def get_page_by_url(self, url):
        return self.filter(lambda page: page.url == url)

    def filter(self, filter):
        if not callable(filter):
            raise TypeError('The filter must be callable')

        filtered_pages = [page for page in self if filter(page)]
        count_pages = len(filtered_pages)

        if count_pages > 0:
            return filtered_pages[0] if count_pages == 1 else filtered_pages

        return None

    def sort(self, key=None, reverse=False):
        if key is None:
            key = lambda page: page.title

        self.data.sort(key=key, reverse=reverse)

    def __str__(self):
        """ Create the string representation of all pages """
        header = StringUtil.header('Content of Pages')

        content_of_pages = [ str(page) for page in self ]
        return (os.linesep*2).join( [header] + content_of_pages)
