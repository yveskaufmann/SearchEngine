__author__ = 'Yves'

from bs4 import BeautifulSoup
from parser.base import BaseParser
from utils.list import ListUtil

class HTMLParser(BaseParser):
	""" 
		Parser which extract out links and the 
		text from a a given HTML content. 

	"""

	def __init__(self):
		BaseParser.__init__(self)

	def parse(self, text):
		dom = self.parseDocument(text)
		
		self.title = self.get_text_from_element('title')
		self.content = self.get_text_from_element('body')
		
		self.out_links = [link['href'] for link in dom.select('a[href]')]
		self.out_links = ListUtil.to_list_without_duplicated_entries(self.out_links)

	
	def parseDocument(self, text):
		self.dom = BeautifulSoup(text, 'html')
		return self.dom

	def get_text_from_element(self, query, default_value = ''):
		found_element = self.dom.find(query)
		
		if found_element is None: 
			return default_value
		
		return found_element.get_text(strip=True)