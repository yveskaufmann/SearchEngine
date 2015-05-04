import os


class RessourceException(Exception):
	pass

class PathUtil:
	"""
		Handy methods for path handling
	"""

	@staticmethod
	def get_content_from_file(path):

		""" 
			Read and returns the content of file 
			specified by path. If the path isn't a existing file
			a FileNotFoundError will be thrown.
		"""

		PathUtil.ensure_path_exists(path)
		with open(path) as file:
			file_content = file.read()
		return file_content

	@staticmethod
	def ensure_path_exists(path):
		"""
			Throws a FileNotFoundError if the specified 
			path isn't a existing file.
		"""
		if not os.path.exists(path):
			raise FileNotFoundError('The "{0}" path dont exists.'.format(path))

class RessourceUtil:

	"""
		Handy methods for ressource handling.
		By ressource is mean a file in side 
		the directory doc/ressources. 
	"""

	@staticmethod
	def get_ressource_path(ressource_name = None):
		"""
			Returns the path to a specifc ressource or to the ressource folder.
		"""
		ressource_folder = ['docs', 'ressources']

		if ressource_name is not None:
			ressource_folder.append(ressource_name)

		ressource_path = os.path.join(*ressource_folder)

		if os.path.isdir(ressource_path) and not ressource_path.endswith('/'):
			ressource_path+= '/'

		return ressource_path

	@staticmethod
	def get_content_from_ressource(ressource_name):
		""" 
			Read and returns the content of a ressource 
			specified by its ressource_name. If there is
			no such ressource then a RessourceException 
			will be thrown.
		"""
		try:
			ressource_path = RessourceUtil.get_ressource_path(ressource_name)
			return PathUtil.get_content_from_file(ressource_path)
		except FileNotFoundError:
			RessourceUtil.__handleFileNotFoundError(ressource_name)

	@staticmethod
	def ensure_ressource_exists(ressource_name):
		"""
			Throws a RessourceException if the specified ressource
			don't exists.
		"""
		try:
			ressource_path = RessourceUtil.get_ressource_path(ressource_name)
			PathUtil.ensure_path_exists(ressource_path)
		except FileNotFoundError:
			RessourceUtil.__handleFileNotFoundError(ressource_name)

	@staticmethod
	def __handleFileNotFoundError(filename):
		raise RessourceException('The "{0}" ressource dont exists.'.format(filename))








