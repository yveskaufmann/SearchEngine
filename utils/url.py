import urllib

class URLUtils:

	""" 
		Handy methods for url handling 
	"""

	@staticmethod
	def is_url_relative(url):
		""" 
			Check if a url is a relative url
			and returns True in this case.
		"""

		url = urllib.parse.urlparse(url)
		is_relative_url =  not url.scheme or url.netloc
		return is_relative_url

	@staticmethod
	def join_relurl_to_absurl(base_url, url):

		"""
			Returns url as absolute url by using base_url as base
			if url is a relative url. Otherwise returns url. 
		"""

		if URLUtils.is_url_relative(base_url):
			return urllib.parse.urljoin(base_url, url)
		return base_url