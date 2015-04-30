
__author__ = 'Yves'

class BaseParser:
	"""  
		Interface for a parser which extract links and 
		the text only out of a given content 
	"""
	def __init__(self):
		
		"""  
			All out links of the parsed document as relative urls. 
		"""
		self.out_links = []
		
		""" The content of the parsed file which contains only the text """
		self.content = ""
		
		""" The name of the parsed document """
		self.title = ""

	
	def get_out_links(self, base = ""):
		return self.out_links

	def get_text(self):
		return self.content

	def parse(content):
		pass


