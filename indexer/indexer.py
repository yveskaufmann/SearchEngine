
from indexer.lexer import TokenLexer
from model.model import Index

class Indexer:
	""" Build an inverted index from assigned page objects. """

	def __init__(self):
		self.__index = Index()
		self.__already_indexed_pages = set()

	def index_pages(self, *pages):
		""" Index a sequence of pages """
		for page in pages:
			self.index_page(page)

	def index_page(self, page):
		""" Index a single page """
		
		# Prevent that a page is indexed multiple times
		if page.title in self.__already_indexed_pages: 
			return

		lexer = TokenLexer(page)
		for token in lexer.tokens():
			self.__index.register_Token(token, page.title)

		# Memorize already indexed pages by his title
		self.__already_indexed_pages.add(page.title)

	@property
	def index (self):
		""" Returns the complete inverted index """
		return self.__index