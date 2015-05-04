from bs4 import BeautifulSoup

from model.model import Page
from utils.list import ListUtil
from utils.url import URLUtils

class HTMLParser:
	""" 
		Parser which extract out links and the 
		text from a a given HTML content. 
	"""

	def parse(self, text, base_url=''):
		dom = self.parseDocument(text)
		
		page = Page()
		page.title = self.get_text_from_element('title')
		page.content = self.get_text_from_element('body')
		
		read_link = lambda link: URLUtils.join_relurl_to_absurl(base_url, link['href'])

		page.out_links = [ read_link(link) for link in dom.select('a[href]')]
		page.out_links = ListUtil.to_list_without_duplicated_entries(page.out_links)

		return page

	def parseDocument(self, text):
		self.dom = BeautifulSoup(text, 'html')
		return self.dom

	def get_text_from_element(self, query, default_value = ''):
		found_element = self.dom.find(query)
		
		if found_element is None: 
			return default_value
		
		return found_element.get_text(strip=False).strip()


 


