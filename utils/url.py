import urllib

class URLUtils:
	@staticmethod
	def is_url_relative(url):
		url = urllib.parse.urlparse(url)
		is_relative_url =  not url.scheme or url.netloc
		return is_relative_url

	@staticmethod
	def join_relurl_to_absurl(base_url, url):
		if URLUtils.is_url_relative(base_url):
			return urllib.parse.urljoin(base_url, url)
		return base_url