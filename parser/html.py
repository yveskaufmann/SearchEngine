from bs4 import BeautifulSoup
from parser.base import BaseParser

class HTMLParser(BaseParser):
	""" Parser which parse HTML content """

	def __init__(self):
		BaseParser.__init__(self)

	def parse(self, content):
		soup = BeautifulSoup(content, 'html')
		self.title = soup.title.string
		self.content = soup.find('body').get_text()
		for link in soup.find_all('a'):
			self.out_links.append(link.get('href')) 
